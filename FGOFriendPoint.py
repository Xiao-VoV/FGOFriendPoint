import os
import time
import winsound

#其中600表示声音大小，1000表示发生时长，1000为1秒
# adb connect 127.0.0.1:7555 

# 931.4 622.2
# 861.4 753

# adb shell input tap 924.4 629.2
#else:
#    time.sleep(1)
#    print("开始抽卡--->")
#    i = 0
#    for i in range(100):
#        for n in range(8):
#            os.system('adb shell input tap 930.4 622.2')
#            time.sleep(0.18)
#        time.sleep(0.1)
#        os.system('adb shell input tap 861.4 753')
#        time.sleep(0.1)
#        print(f"第 {i+1} 次抽卡！")


print("----------------------------")
print("在<继续进行10次召唤>界面处运行程序!")
print("----------------------------")
port = str(input("输入要连接的端口号:>"))
if port.isdigit():
    print('will connect 127.0.0.1:'+port)
else:
    port = '7555 '
if os.system('adb connect 127.0.0.1:'+port) != 0:
    print("连接错误！")
else:
    print("----------开始抽卡----------")
    i = 0
    count  = int(input("输入要抽卡的次数:>"))

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
        print(f"第 {i+1} 次抽卡！")

#记录结束时间
endtime = time.time()

dtime = endtime - starttime
print("\n*******抽卡结束！耗时 %.4s s *******" % dtime)

#声音提醒
a = 0
for a in range(4):
    winsound.Beep(1000,500)
    time.sleep(0.5)
os.system('adb kill-server')
