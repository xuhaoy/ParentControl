echo off
netstat -ano | find "CLOSE_WAIT" > out.txt

FOR /F "tokens=5 delims= " %%I IN (out.txt) DO (
    TASKKILL %%I
)

del out.txt
