import os
import  time
# adb connect 127.0.0.1:7555 

# 931.4 622.2
# 861.4 753

# adb shell input tap 924.4 629.2

if os.system('adb connect 127.0.0.1:7555') != 0:
    print("连接错误！")
else:
    time.sleep(3)
    print("开始抽卡--->")
    i = 0
    for i in range(50):
        for n in range(7):
            os.system('adb shell input tap 930.4 622.2')
            time.sleep(0.2)
        os.system('adb shell input tap 861.4 753')
        time.sleep(0.3)
        print(f"第 {i+1} 次抽卡！")
print("抽卡结束！")
os.system('adb kill-server')
