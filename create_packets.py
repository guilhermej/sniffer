#####################################
# Python para Pentesters            #
# https://solyd.com.br/treinamentos #
#####################################

## SYN TCP PORT SCAN

from scapy.all import *

ports = [80,8080,22,21,3306,25]
hosts = ['facebook.com', 'solyd.com.br', 'www.ufu.br']

pacote = IP(dst=hosts)/TCP(dport=ports, flags='S')

recebido, nao_recebido = sr(pacote, timeout=1)

for n in range(len(recebido)):
    print recebido[n][0][IP].dst, ":", recebido[n][0][TCP].dport
