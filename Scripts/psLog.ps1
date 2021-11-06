Function checkProcesses {
    $fileName = "C:\ParentControl\logs\processes_"

    $fileName += $(Get-Date -Format "yyyy/MM/dd-HHmmss")

    $fileName += ".log"

    ps > $fileName

	ps geforce*
	ps steam*
	ps minecraft*
	ps roblox*
	ps terraria*
}

Function killOffendingProcesses {
	taskkill /im geforce* /f
	taskkill /im steam* /f
	taskkill /im minecraft* /f
	taskkill /im roblox* /f
	taskkill /im terraria* /f
}