import os
import  time
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
if os.system('adb connect 127.0.0.1:7555') != 0:
    print("连接错误！")
else:
    print("*******开始抽卡*******")
    i = 0
    count  = int(input("输入要抽卡的次数:>"))
    for i in range(count):
        os.system('adb shell input tap 852.4 761.0')
        #time.sleep(0.05)
        os.system('adb shell input tap 937.2 637.2')
        j = 0
        time.sleep(2)
        for j in range(3):
            os.system('adb shell input tap 1288.0 599.2')
            time.sleep(0.13)
        time.sleep(0.3)
        print(f"第 {i+1} 次抽卡！")


print("\n*******抽卡结束！*******")
os.system('adb kill-server')
