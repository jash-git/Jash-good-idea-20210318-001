Windows 設定預約自動關機

資料來源: https://www.kjnotes.com/windows/2

首先可以先了解Windows常用的shutdown關機指令有哪些：
-s → 將電腦關閉。
-t xxxx → 倒數計時，單位為秒，有效範圍是0~315360000（十年），預設值是30秒。
-f → 強制關閉執行中的應用程式，而不事先警告使用者。當 /t 參數大於0值時，會隱含 /f 參數。
-a → 取消自動關機指令。
shutdown -a 這指令意思是：將取消自動關機的指令。
shutdown /? → 假如想要了解更多Windows的關機指令，那可以在cmd或PowerShell中輸入『shutdown /?』。

EX: shutdown -s -t 3600 這指令意思是：電腦將在1小時後自動關機。

完整教學:

