import argparse, socket

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target', type=str, required=True)
parser.add_argument('-p', '--ports', type=str,required=True)
parser.add_argument('-tcp', '--tcp', type=str, required=False)
parser.add_argument('-udp', '--upd', type=str, required=False)
args = parser.parse_args()
ip = args.target
list_ports = args.ports
ports = list_ports.split(',')
tcp_args = args.tcp
 
def scanTCP():
 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketClient: 
  for i in ports:
     port = int(i)
     socketClient.settimeout(0.5)
     result = socketClient.connect_ex((ip,port))
     if result == 0:
       print('Porta aberta')
     else:
      print('Porta fechada ou filtrada')
     socketClient.close()


if tcp_args:
    scanTCP()

else:
   print('teste')