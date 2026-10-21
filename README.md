# PTT Soft_Job 軟體工程情報爬蟲

這是一個使用 Python 開發的網路爬蟲工具，自動擷取 PTT `Soft_Job`（軟體工作版）的最新文章，並根據指定關鍵字篩選出求職、面試、Python 相關情報，自動將資料寫入或追加至 CSV 檔案中。

---

## 📌 功能特色
* **自動過濾關鍵字**：篩選包含「徵才」、「Junior」、「Python」、「職缺」、「面試」、「分享」等主題文章。
* **資料累積儲存**：結果會自動存入 `tech_job_reports.csv`，支援追加（Append）模式，避免覆蓋舊資料。
* **防亂碼設計**：匯出時使用 `utf-8-sig` 編碼，使用 Excel 開啟 CSV 時不會出現中文亂碼。
* **執行預覽**：程式執行完畢後會在終端機（Terminal/Console）顯示抓取結果摘要與文章連結。

---

## 🛠️ 環境與套件需求
* **Python 3.x**
* **第三方套件**：
  * `requests`：處理 HTTP 網頁請求
  * `beautifulsoup4`：解析 HTML 結構

### 安裝必要套件
請在終端機或命令提示字元（CMD）執行以下指令：
```bash
pip install requests beautifulsoup4
