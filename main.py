import socket
import re

print("         />_________________________________ ")
print("[########[]_________________________________>")
print("         \>                                   \n")
print("                      __                                  ___________           .__")
print("______   ____________/  |_    ______ ____ _____    ____   \__    ___/___   ____ |  |")
print("\____ \ /  _ \_  __ \   __\  /  ___// ___\\__  \  /    \    |    | /  _ \ /  _ \|  | ")
print("|  |_> >  <_> )  | \/|  |    \___ \\  \___ / __ \|   |  \   |    |(  <_> |  <_> )  |__")
print("|   __/ \____/|__|   |__|   /____  >\___  >____  /___|  /   |____| \____/ \____/|____/")
print("|__|                             \/     \/     \/     \/                              \n")

host = input("Write the HOST/IP: ")

# validando IP fornecido
padrao_ipv4 = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

if re.match(padrao_ipv4, host):
    host_flag = True
else:
    print("O ip nao esta correto!")
    host_flag = False

ports = [21, 22, 23, 25, 53, 80, 111, 135, 139, 445, 3306, 8080, 9090, 443]
cond = input("Você quer utilizar as portas padrões?[S/N] ").upper().strip()

# tratando dados de entrada
if cond.isalpha():
    flag = True
else:
    flag = False

if flag and host_flag:
    if cond == 'N':
        ports = []
        ports = [int(x) for x in input(
            "Digite as portas que voce quer verificar: ").split()]

    print("\n[+] Starting port scanning...\n")

    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        code = client.connect_ex((host, port))
        if code == 0:
            print(f"[+] Port {port} is open!")
        else:
            print(f"[+] Port {port} is closed!")

print("\n[+] Port scanning is finished")
