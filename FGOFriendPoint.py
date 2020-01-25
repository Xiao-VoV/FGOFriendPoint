import os
import  time
# adb connect 127.0.0.1:7555

# 931.4 622.2
# 861.4 753

# adb shell input tap 924.4 629.2

#os.system('adb connect 127.0.0.1:7555')
#time.sleep(6)
i = 0
for i in range(101):
    for n in range(8):
        os.system('adb shell input tap 930.4 622.2')
        time.sleep(0.2)
    os.system('adb shell input tap 861.4 753')
    time.sleep(0.5)
    print(f"第 {i+1} 次抽卡！")
