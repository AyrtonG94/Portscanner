import socket
ip = socket.gethostbyname(input("Digite o ip ou url do alvo:\n"))
nome_log = input("Digite o nome do arquivo de log: \n")

with open("lista_ips.txt", "r", encoding="utf-8") as arquivo:
     lista_portas = arquivo.read()
     nova_lista = map(int, lista_portas.split())
     for portas in nova_lista:
          conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          conexao.settimeout(0.5)
          resultado = conexao.connect_ex((ip, portas))
          if resultado == 0:
               print (f"[+] Porta aberta: {portas}")
               with open(f"{nome_log}.txt", "a", encoding="utf-8") as arquivo:
                    arquivo.write(f"Porta aberta: {portas} \n")
          else:
               print(f"[-] Porta fechada: {portas}")
               with open(f"{nome_log}.txt", "a", encoding="utf-8") as arquivo:
                    arquivo.write(f"Porta fechada: {portas} \n")
          conexao.close()     

print("Scanner finalizado")