C:\Program Files (x86)\LogMeIn Hamachi\x64\hamachi-2.exe --cli go-online 400-688-873

netstat -abno > %cd%\Connections_%date:~-4,4%%date:~-10,2%%date:~-7,2%_%time:~0,2%%time:~3,2%%time:~6,2%.txt

netstat -abno > C:\Users\Xuhao\Documents\github\ParentControl\logs\Connections_%date:~-4,4%%date:~-10,2%%date:~-7,2%_%time:~0,2%%time:~3,2%%time:~6,2%.txt

ps application_name

taskkill /im name* /f

ps > $(Get-Date -Format "yyyy/MM/dd-HHmmss")