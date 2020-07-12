import os
import time
import winsound


if os.system('adb connect 127.0.0.1:7555') != 0:
    print("连接错误！")
else:
    #print("----------开始抽卡----------")
    i = 0
    count  = 50

    #记录开始时间
    starttime = time.time()

    for i in range(count):
        os.system('adb shell input tap 852.4 761.0')
        #time.sleep(0.05)
        os.system('adb shell input tap 937.2 637.2')
        j = 0
        time.sleep(2)
        for j in range(3):
            os.system('adb shell input tap 1288.0 599.2')
            time.sleep(0.1)
        time.sleep(0.28)
        #print(f"第 {i+1} 次抽卡！")

#记录结束时间
endtime = time.time()

dtime = endtime - starttime
#print("\n*******抽卡结束！耗时 %.4s s *******" % dtime)

#声音提醒
a = 0
for a in range(4):
    winsound.Beep(1000,500)
    time.sleep(0.5)
os.system('adb kill-server')
