import time
import datetime
from datetime import date
import subprocess


CHECK_INTERVALS = 10
NUM_WEEKDAY_TOKENS = 2*3600 / 10
NUM_WEEKEND_TOKENS = 3*3600 / 10
LOGS_FOLDER_PATH = "C:/Users/Xuhao/Documents/github/ParentControl/logs/"
POWERSHELL_PATH = "C:/WINDOWS/system32/WindowsPowerShell/v1.0/powershell.exe"
POWERSHELL_SCRIPTS_PATH = "C:/Users/Xuhao/Documents/github/ParentControl/Scripts/"

# run every 5 seconds to check if a specified program is running
def psChecker():
    # run the script to check for a specific process
    ps = subprocess.Popen([POWERSHELL_PATH,
                           '-ExecutionPolicy',
                           'Unrestricted',
                           POWERSHELL_SCRIPTS_PATH + 'checkProcesses.ps1'])
    result = ps.wait()
    # output the process as a log
    return False

# logs onto log file about how many tokens used over the threshold
# this function will not terminate the offending processes
def tokenSaturatedWarn(tokensExceeded):
    today = datetime.datetime.now().strftime("%Y%m%d")
    warningFile = open(LOGS_FOLDER_PATH + "WARNINGS_" + today + ".txt", "a")
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    warningFile.write(timestamp + "Time Exceeded: " + tokensExceeded * 10 + " seconds\n")
    warningFile.close()

# function for when the user saturates the tokens available for the day
# this function will terminate the offending processes
def killOffendingProcesses():
    ps = subprocess.Popen([POWERSHELL_PATH,
                           '-ExecutionPolicy',
                           'Unrestricted',
                           POWERSHELL_SCRIPTS_PATH + 'KillOffendingProcesses.ps1'])
    result = ps.wait()
    
if __name__ == "__main__":
    # open the previous log file
    # open the application state file
    dayOfWeek = datetime.datetime.today().isoweekday()
    tokensRemaining = NUM_WEEKDAY_TOKENS if (dayOfWeek < 5) else NUM_WEEKEND_TOKENS
    today = datetime.datetime.now().strftime("%Y%m%d")
    
    # run every 5 seconds to check if a specified program is running
    while(True):
        #time.sleep(10)
        # if new day
        if (datetime.datetime.today().isoweekday() != dayOfWeek):
            today = datetime.datetime.now().strftime("%Y%m%d")
            # reset the number of tokens
            dayOfWeek = datetime.datetime.today().isoweekday()
            tokensRemaining = NUM_WEEKDAY_TOKENS if (dayOfWeek < 5) else NUM_WEEKEND_TOKENS
        if (psChecker()):
            
            tokensRemaining -= 1
            #if (tokensRemaining < 0):
                # ran out of tokens to play run script to kill offending processes

        time.sleep(10)