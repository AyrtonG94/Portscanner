import socket
ip = input("Digite o ip alvo:\n")
print("Carregando o arquivo lista_ips.txt: \n")
with open("lista_ips.txt", "r", encoding="utf-8") as arquivo:
     lista_portas = arquivo.read()
     nova_lista = map(int, lista_portas.split())
     for portas in nova_lista:
          conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          conexao.settimeout(0.5)
          resultado = conexao.connect_ex((ip, portas))
          if resultado == 0:
               print (f"[+] Porta aberta: {portas}")
          else:
               print(f"[-] Porta fechada: {portas}")
          conexao.close()
print("Scanner finalizado")