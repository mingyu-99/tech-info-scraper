# PTT Soft_Job 軟體工程職缺與情報爬蟲

這是一個使用 Python 開發的網路爬蟲工具，自動擷取 PTT `Soft_Job`（軟體工作版）的最新文章，並根據指定關鍵字篩選出與求職、面試、Python 相關的重要情報，最終自動輸出並累積儲存至 CSV 檔案中。

## 功能特色
- **自動過濾**：自動針對「徵才」、「Junior」、「Python」、「職缺」、「面試」、「分享」等關鍵字進行標題篩選。
- **資料持久化**：抓取結果會自動存入 `tech_job_reports.csv`，支援資料追加（Append）模式，方便累積長期數據。
- **防亂碼處理**：使用 `utf-8-sig` 編碼，在 Excel 中開啟 CSV 檔案時不會產生中文亂碼。

## 使用的 Python 套件
- `requests` (網頁請求)
- `BeautifulSoup` (網頁解析)
- `csv` (資料輸出)
- `os` / `datetime` (檔案檢查與時間標記)

## 快速開始
1. 確保您的環境已安裝 Python 與必要套件：
   ```bash
   pip install requests beautifulsoup4
