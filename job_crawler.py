import requests
from bs4 import BeautifulSoup
import csv
import os
from datetime import datetime

def fetch_and_export_to_csv():
    print("正在檢索最新軟體工程相關討論與情報...")
    
    # PTT 工作版
    url = "https://www.ptt.cc/bbs/Soft_Job/index.html"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            print("無法存取網站，狀態碼：", response.status_code)
            return
            
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('div', class_='r-ent')
        
        results = []
        # 關鍵字
        keywords = ["徵才", "Junior", "Python", "職缺", "面試", "分享"]
        
        for article in articles:
            title_div = article.find('div', class_='title')
            if title_div and title_div.a:
                title = title_div.a.text.strip()
                link = "https://www.ptt.cc" + title_div.a['href']
                date = article.find('div', class_='date').text.strip()
                author = article.find('div', class_='author').text.strip()
                
                # 檢查標題是否包含關鍵字
                if any(kw.lower() in title.lower() for kw in keywords):
                    results.append({
                        "日期": date,
                        "標題": title,
                        "作者": author,
                        "連結": link,
                        "抓取時間": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
        
        print("共找到", len(results), "筆符合關鍵字的情報！")
        
        if results:
            # CSV 檔案名稱
            csv_filename = "tech_job_reports.csv"
            file_exists = os.path.isfile(csv_filename)
            
            
            with open(csv_filename, mode='a', newline='', encoding='utf-8-sig') as file:
                fieldnames = ["日期", "標題", "作者", "連結", "抓取時間"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                
                # 如果是新檔案,先寫入標題列 (Header)
                if not file_exists:
                    writer.writeheader()
                
                # 寫入抓到的數據
                for row in results:
                    writer.writerow(row)
                    
            print("資料已成功寫入/追加至", csv_filename, "檔案中！")
            
            #最終預覽
            print("\n抓取結果預覽：")

            for idx, item in enumerate(results, 1):
                author_name = item['author'] if 'author' in item else item['作者']
                print(idx, ". [", item['日期'], "] ", item['標題'], " (作者: ", author_name, ")", sep="")
                print("   連結:", item['連結'])
            
    except Exception as e:
        print("發生錯誤:", e)

if __name__ == "__main__":
    fetch_and_export_to_csv()