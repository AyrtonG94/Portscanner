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

def scanTCP():

 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketCliente: 
  for i in ports:
     port = int(i)
     socketCliente.settimeout(0.5)
     result = socketCliente.connect_ex((ip,port))
     if result == 0:
          print('Porta aberta')
     else:
          print('Porta fechada ou filtrada')
          
     socketCliente.close()