import time

CHECK_INTERVALS = 10
NUM_WEEKDAY_TOKENS = 2*3600 / 10
NUM_WEEKEND_TOKENS = 3*3600 / 10


# run every 5 seconds to check if a specified program is running
def psChecker():
    # run the script to check for a specific process
    # output the process as a log
    return False

if __name__ == "__main__":
    dayOfWeek = datetime.datetime.today().isoweekday()
    tokensRemaining = NUM_WEEKDAY_TOKENS if (dayOfWeek < 5) else NUM_WEEKEND_TOKENS

    # run every 5 seconds to check if a specified program is running
    while(True):
        # if new day
        if (datetime.datetime.today().isoweekday() != dayOfWeek):
            # reset the number of tokens
            dayOfWeek = datetime.datetime.today().isoweekday()
            tokensRemaining = NUM_WEEKDAY_TOKENS if (dayOfWeek < 5) else NUM_WEEKEND_TOKENS
        if (psChecker()):

            tokensRemaining -= 1
            if (tokensRemaining < 0):
                # ran out of tokens to play run script to kill offending processes

        time.sleep(10)
