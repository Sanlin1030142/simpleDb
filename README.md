# Database.py

這個檔案包含了與資料庫相關的六個基礎操作以及Set Intersection。

## 使用方法

1. 確保你已經安裝了 pandas，這是這個檔案的唯一依賴項目。你可以使用以下的命令來安裝 pandas：

```bash
pip install pandas
```


## 功能
- 執行六個小指令 select, project, rename, cartesian product, set union, set difference
- 執行一個進階指令 set intersection
- 提供一些方便的小工具如輸出、刪除、重載入表格
- 處理資料庫輸入所導致錯誤


## 注意事項
- 程式會在 /inputtable 裡面找到 majors 跟 students 兩個輸入檔案，使用者**不須做初始載入**(tools.No11)
- 程式在首次啟動時會輸出可使用的table名稱及內容，以供使用者參考
- 在每一次執行指令前會輸出指令列表，使用者可以輸入指令號碼選擇功能
- 程式除了刪除的**所有**輸出表格都會以一個新的表格呈現，不會動到原始資料
- 其他的注意事項會在使用過程中做出提示，請安心使用
