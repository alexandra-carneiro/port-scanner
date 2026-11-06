# Scanner de portas em Python
# Verifica se uma porta está aberta num anfitrião
# Usa só nas tuas máquinas ou em redes que tens autorização para testar

import socket


def porta_aberta(anfitriao, porta):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((anfitriao, porta))
        s.close()
        return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False


anfitriao = input("Indica o anfitrião (IP ou nome) ")
porta = int(input("Indica a porta "))

if porta_aberta(anfitriao, porta):
    print(f"A porta {porta} está aberta em {anfitriao}")
else:
    print(f"A porta {porta} está fechada ou filtrada em {anfitriao}")

# Próximo passo, ler uma lista de portas comuns e testar uma a uma com um ciclo for
