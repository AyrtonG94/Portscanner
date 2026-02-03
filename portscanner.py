import socket
import threading
ip = socket.gethostbyname(input("Digite o ip ou url do alvo:\n"))
nome_log = input("Digite o nome do arquivo de log: \n")

def scan_tcp():
     with open("portas_TCP.txt", "r", encoding="utf-8") as arquivo:
          lista_portas = arquivo.read()
          nova_lista = map(int, lista_portas.split())
          for portas in nova_lista:
               conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               conexao.settimeout(1)
               resultado = conexao.connect_ex((ip, portas))
               if resultado == 0:
                    print (f"[+] Porta TCP aberta: {portas}")
                    with open(f"{nome_log}.txt", "a", encoding="utf-8") as arquivo:
                         arquivo.write(f"Porta aberta: {portas} \n")
               else:
                    print(f"[-] Porta TCP fechada: {portas}")
                    with open(f"{nome_log}.txt", "a", encoding="utf-8") as arquivo:
                         arquivo.write(f"Porta fechada: {portas} \n")
               conexao.close()     

def scan_upd():
     with open("portas_UDP.txt", "r", encoding="utf-8") as arquivo:
          lista_portas = arquivo.read()
          nova_lista = map(int, lista_portas.split())
          for porta in nova_lista:
            conexao = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            conexao.settimeout(1)

            try:
                    conexao.sendto(b"scan", (ip, porta))
                    dados, _ = conexao.recvfrom(1024)

                    print(f"[+] Porta UDP aberta: {porta}")
                    with open(f"{nome_log}.txt", "a", encoding="utf-8") as log:
                         log.write(f"Porta UDP aberta: {porta}\n")

            except socket.timeout:
                    print(f"[?] Porta UDP filtrada ou aberta (sem resposta): {porta}")
                    with open(f"{nome_log}.txt", "a", encoding="utf-8") as log:
                         log.write(f"Porta UDP filtrada ou aberta: {porta}\n")

            except OSError:
                    print(f"[-] Porta UDP fechada: {porta}")
                    with open(f"{nome_log}.txt", "a", encoding="utf-8") as log:
                         log.write(f"Porta UDP fechada: {porta}\n")

            finally:
                    conexao.close()

t1 = threading.Thread(None, scan_tcp, 't1')
t2 = threading.Thread(None, scan_upd, 't2')
t1.start()
t2.start()