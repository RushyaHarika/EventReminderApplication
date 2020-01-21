import time
import os
def checkTodaysEvents():
    f=open("EventFile.txt",'r')
    today=time.strftime('%m%d')
    flag=0
    for line in f:
        if today in line:
            line=line.split(' ')
            s=''
            for i in range(1,len(line)):
                s+=line[i]
                s+=" "
            flag=1
            os.system('notify-send "Events Today: '+s+'"')
    if flag==0:
        os.system('notify-send "No Events Today!"')
if __name__=="__main__":
    checkTodaysEvents()
