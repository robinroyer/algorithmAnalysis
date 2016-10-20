import sys

# Function to return an arg if provided to the script
# 
# @{number}: number of the arg in sys.argv
def getArgv(number):
    try:
        sys.argv[number]
    except IndexError:
        return ""
    else:
        return sys.argv[number]