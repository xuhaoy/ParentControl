Function checkProcesses {
    $fileName = "C:\Users\Xuhao\Documents\github\ParentControl\logs\processes_"

    $fileName += $(Get-Date -Format "yyyy/MM/dd-HHmmss")

    $fileName += ".log"

    ps > $fileName

    ps geforce*
    ps steam*
}

Function killOffendingProcesses {
    taskkill /im geforce* /f
    taskkill /im steam* /f
}