$fileName = "C:\ParentControl\logs\processes_"

$fileName += $(Get-Date -Format "yyyy/MM/dd-HHmmss")

$fileName += ".log"

ps > $fileName

ps geforce*
ps steam*
ps minecraft*
ps roblox*
ps terraria*