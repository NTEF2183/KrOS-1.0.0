import time

print('Loading Files... (49KB/1024KB)')
time.sleep(1)
print('Loading Files... (325KB/1024KB)')
time.sleep(1)
print('Loading Files... (1024KB/1024KB)')
time.sleep(3)
print('Loading Forge Files... (144KB/14000KB)')
time.sleep(1)
print('Loading Forge Files... (1460KB/14000KB)')
time.sleep(1)
print('Loading Forge Files... (7102KB/14000KB)')
time.sleep(1)
print('Loading Forge Files... (14000KB/14000KB)')
time.sleep(3)
print('Loading KrOS... (17KB/19250KB)')
time.sleep(1)
print('Loading KrOS... (1560KB/19250KB)')
time.sleep(1)
print('Loading KrOS... (7368KB/19250KB)')
time.sleep(5)
print('Welcome to KrOS!')
time.sleep(3)
while True:
    a = input('''
              Which file do you want to open?
              This Computer
              White Board
              Colorful Eggs
              Internet Explorer
              Shutdown
              CMD
              Intel(R) HD Graphics Seetings
              ''')
    if (a == 'This Computer'):
        print('''
                      Intel Core i5-2410
                      NVIDIA GeForce GTS 450
                      4GB DDR3
                      240GB HDD
                      KrOS 0.9.9 Pro
                      Internet:False
                      ''')
        time.sleep(6)
        continue
    elif (a == 'White Board') :
        print('The whiteboard is temporarily unavailable.')
        time.sleep(3)
        continue
    elif (a == 'Colorful Eggs') :
        print('''
                      KrOS crashes due to Forge library crash
                      It has crashed now
                      Please reinstall the new Forge
                      library URL: https://www.bluesheep.com/en-us/forgeURL/Forge-en-us-1.0.0.0335/
              ''')
        time.sleep(5)
        break
    elif a==("Internet Explorer"):
        print("The Internet is False!")
        time.sleep(5)
        continue
    elif a==("CMD"):
        while True:
            b=input("You can enter commands on your own However, KrOS only has a few commands at present")
            if b==("KrOComputer_d"):
                print("""
                     Intel Core i5-2410
                      NVIDIA GeForce GTS 450
                      4GB DDR3
                      240GB HDD
                      KrOS 0.9.9 Pro
                      Internet:False
                     """)
                time.sleep(3)
                continue
            elif b==("KrInternetw"):
                print("""
                      TP-LINK-40N6
                      HUAWEI-34N
                      iPhone(4)
                      CMCC-8kP2
                     """)
                time.sleep(3)
                continue
            elif b==("KrPresForge"):
                print("Forge Version:1.0.0.0336Pre")
                time.sleep(3)
                continue
            elif b==("KrPresForge_d"):
                print("""
                      KrOS crashes due to Forge library crash
                      It has crashed now
                      Please reinstall the new Forge
                      library URL: https://www.bluesheep.com/en-us/forgeURL/Forge-en-us-1.0.0.0335/
                     """)
                time.sleep(3)
                break
            elif b==("Exit"):
                break
            elif b==("KrIntelHDs"):
                print("Intel (R) HD Graphics Seeting Loading...  1024KB/8192KB")
                time.sleep(3)
                print("Intel (R) HD Graphics Seeting Loading...  4108KB/8192KB")
                time.sleep(3)
                while True:
                    d=input("""
Intel HD Graphics Seeting
Which setting do you want?
    3D Seetings
    resolution
    Video
    Exit
                          """)
                    if d==("3D"):
                        print("The 3D option is temporarily unavailable")
                        time.sleep(3)
                        continue
                    elif d==("resolution"):
                        e=input("What resolution do you want to tune to?Current resolution: 1920*1080")
                        if e==("1600*900"):
                            print("Loading...")
                            time.sleep(5)
                            print("OK!")
                            continue
                        elif e==("1920*991"):
                            print("Loading...")
                            time.sleep(1)
                            print("OK!")
                            continue
                    if d==("Video"):
                        f=input("Which refresh rate do you want?")
                        rd=("120 Hz")
                        if f==("60 Hz") and f!=rd:
                            print("Loading")
                            time.sleep(3)
                            print("OK")
                            rd=f
                            continue
                        elif f==("120 Hz") and f!=rd:
                            print("Loading")
                            time.sleep(1)
                            print("OK")
                            rd=f
                            continue
                        elif f==("240 Hz") and f!=rd:
                            print("Loading")
                            time.sleep(2)
                            print("OK")
                            rd=f
                            continue
                        elif f==rd:
                            print("It's already this refresh rate")
                            time.sleep(2)
                            #GUYIFANGSHUI
                            continue
                    elif d==("Exit"):
                        break
            elif b==("KrBugsCreacil"):
                print("""
These are all bugs and changelogs fixed by KrOS
0.9.8
    KrOS 0.3.6 Enternint
    KrOS Security Patch [2024#7]
0.9.9
    KrOS Security Patch [2024#8]
    KrOS Python's Originds
    KrOS Security Patch [2024#9]
    Intel HD Graphics KB-R150KH835M2
    KrOS Python's for Intel HD Graphics Seetings App
1.0.0
    KrOS Security Patch [2024#10]
    KrOS Python's Interander
                        """)
            else:
                print("They are NOT True")
                time.sleep(3)
                continue
    elif a==("Intel(R) HD Graphics Seetings"):
         print("Intel (R) HD Graphics Seeting Loading...  1024KB/8192KB")
         time.sleep(3)
         print("Intel (R) HD Graphics Seeting Loading...  4108KB/8192KB")
         time.sleep(3)
         while True:
                    d=input("""
Intel HD Graphics Seeting
Which setting do you want?
    3D Seetings
    resolution
    Video
    Exit
                          """)
                    if d==("3D"):
                        print("The 3D option is temporarily unavailable")
                        time.sleep(3)
                        continue
                    elif d==("resolution"):
                        e=input("What resolution do you want to tune to?Current resolution: 1920*1080")
                        if e==("1600*900"):
                            print("Loading...")
                            time.sleep(5)
                            print("OK!")
                            continue
                        elif e==("1920*991"):
                            print("Loading...")
                            time.sleep(1)
                            print("OK!")
                            continue
                    if d==("Video"):
                        f=input("Which refresh rate do you want?")
                        rd=("120 Hz")
                        if f==("60 Hz") and f!=rd:
                            print("Loading")
                            time.sleep(3)
                            print("OK")
                            rd=f
                            continue
                        elif f==("120 Hz") and f!=rd:
                            print("Loading")
                            time.sleep(1)
                            print("OK")
                            rd=f
                            continue
                        elif f==("240 Hz") and f!=rd:
                            print("Loading")
                            time.sleep(2)
                            print("OK")
                            rd=f
                            continue
                        elif f==rd:
                            print("It's already this refresh rate")
                            time.sleep(2)
                            #GUYIFANGSHUI
                            continue
                    elif d==("Exit"):
                        break
    elif a==("Shutdown"):
        c=input("Shutdown?")
        if c==("Yes"):
            print("Loading Shutdown Forge and KrOS")
            time.sleep(3)
            print("See you again!")
            time.sleep(5)
            break
