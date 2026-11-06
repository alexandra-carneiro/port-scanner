# Scanner de portas em Python

Ferramenta simples para verificar que portas estão abertas num anfitrião. Escrita em Python, com sockets.

## Estado

Em desenvolvimento. A primeira versão verifica uma porta de cada vez. O próximo passo é ler uma lista de portas comuns e testar uma a uma.

## Como funciona

O programa tenta ligar-se a uma porta com um socket TCP. Se a ligação resulta, a porta está aberta. Se a ligação falha, a porta está fechada ou filtrada.

## Como usar

Corre o programa com Python 3 e indica o anfitrião e a porta.

```text
python3 scanner.py
```

## Regra de uso

Usa esta ferramenta só nas tuas máquinas ou em redes que tens autorização para testar. Nunca faças varreduras a máquinas que não são tuas.

## O que estou a praticar

Python, com sockets, ciclos e tratamento de erros, e redes, com TCP e portas.

## Ficheiros

- scanner.py, a ferramenta
- README.md, este ficheiro
