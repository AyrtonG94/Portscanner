import argparse, socket, concurrent.futures

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target', type=str, required=True)
parser.add_argument('-p', '--ports', type=str,required=True)
parser.add_argument('-tcp', '--tcp', action='store_true')
parser.add_argument('-udp', '--upd', action='store_true')
parser.add_argument('-threads', '--threads', type=int, required=True)
args = parser.parse_args()
ip = args.target
list_ports = args.ports
ports = list_ports.split('-')
ports = range(int(ports[0]), int(ports[1]) + 1)

def scanTCP(port):
       with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketClient: 
        socketClient.settimeout(0.5) 
        result = socketClient.connect_ex((ip,port))    
        if result == 0:
          try:
            bannerGrab = socketClient.recv(1024)
            print(f"Porta {port} aberta -  Serviço: {bannerGrab.decode('latin_1').strip()}")
            return f"Porta {port}: {bannerGrab.decode('latin_1').strip()}"
          except (socket.timeout, TimeoutError):
            print(f'Porta {port} aberta (Serviço Silencioso)')
            return  f"Porta: {port} Serviço Silencioso"
 
if args.tcp and args.upd:
    print('Você não pode usar TCP e UDP ao mesmo tempo')
elif args.tcp:
  with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
    results = executor.map(scanTCP, ports)
  with open('resultado.txt', 'w') as file:
    for i in results:
      if i:
       file.write(f'{i} \n')
      
