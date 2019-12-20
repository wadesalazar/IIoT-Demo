import time, sys
import subprocess 


def getState():
    log = subprocess.call(["powershell.exe", "date"], stdout=sys.stdout)
    log2 = subprocess.call("hostname", stdout=sys.stdout)
    log3 = subprocess.call("ping -n 1 8.8.8.8")



    return 0

if __name__ == "__main__":
    
    getState()

    pass 
    






