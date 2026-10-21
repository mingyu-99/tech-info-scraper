# 🕷️ 軟體情報自動化抓取與 CSV 報表匯出工具

這是一個基於 Python 打造的網頁爬蟲工具，能自動檢索 Soft_Job 版面上的關鍵字情報，並將結果格式化導出至 CSV 報表檔中。

## 🌟 核心功能
- **資料擷取**：自動解析 PTT 文章列表，擷取日期、標題、作者與文章連結。
- **關鍵字過濾**：可自訂關注主題（如：徵才、Junior、Python、面試），精準篩選目標內容。
- **資料持久化**：支援自動新增與追加模式寫入 CSV，並採用 `utf-8-sig` 編碼避免 Excel 開啟時中文亂碼。

## 🛠️ 使用技術
- **Language**: Python
- **Libraries**: Requests, BeautifulSoup4, CSV, Datetime

## 🚀 本地端執行步驟

1. Clone 本專案：
```bash
https://github.com/mingyu-99/tech-info-scraper.git
cd tech-info-scraper
