import argparse, socket, concurrent.futures, ipaddress

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target', type=str, required=True)
parser.add_argument('-p', '--ports', type=str,required=True)
parser.add_argument('--tcp', action='store_true')
parser.add_argument('--udp', action='store_true')
parser.add_argument('--threads', type=int, required=True)
args = parser.parse_args()
ip = args.target
list_ports = args.ports
ports = list_ports.split('-')
ports = range(int(ports[0]), int(ports[1]) + 1)

def scan_tcp(port: int) -> str:
       with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_client: 
        socket_client.settimeout(0.5) 
        result = socket_client.connect_ex((ip,port))    
        if result == 0:
          try:
            banner_grab = socket_client.recv(1024)
            print(f"Porta {port} aberta -  Serviço: {banner_grab.decode('latin_1').strip()}")
            return f"Porta {port}: {banner_grab.decode('latin_1').strip()}"
          except (socket.timeout, TimeoutError):
            print(f'Porta {port} aberta (Serviço Silencioso)')
            return  f"Porta: {port} Serviço Silencioso"

if args.tcp and args.udp:
    exit('Você não pode usar TCP e UDP ao mesmo tempo')
    
if not args.target:
  exit('Obrigatório especificar um endereço de IP')

try:
	str(ipaddress.ip_address(ip))
except ValueError as erro:
    print(f'Digite um enderço de ip válido {erro}')
    
if args.tcp:
     with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
      results = executor.map(scan_tcp, ports)
      with open('resultado.txt', 'w') as file:
        for i in results:
         if i:
          file.write(f'{i} \n')
