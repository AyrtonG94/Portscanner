import argparse, socket

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target', type=str, required=True)
parser.add_argument('-p', '--ports', type=str,required=True)
parser.add_argument('-tcp', '--tcp', type=str, required=False)
parser.add_argument('-udp', '--upd', type=str, required=False)
args = parser.parse_args()
ip = args.target
list_ports = args.ports
ports = list_ports.split('-')
 
def scanTCP():
 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketClient: 
  for i  in ports:
    port = int(i)
    socketClient.settimeout(1.0) 
    result = socketClient.connect_ex((ip,port))
    if result == 0 :
      teste = socketClient.recv(1024)
      print(f'Porta {port} aberta', teste.decode())
    else:
      print('Porta fechada ou filtrada')
 socketClient.close()


if args.tcp and args.upd:
    print('Você não pode usar TCP e UDP ao mesmo tempo')
elif args.tcp:
  scanTCP()
else:
   print(list(range(1, 80)))
   