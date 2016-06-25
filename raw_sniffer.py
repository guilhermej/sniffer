#####################################
# Python para Pentesters            #
# https://solyd.com.br/treinamentos #
#####################################

import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

#s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3)) # Capture Ether

#s.bind(('', 0))

while True:
    pacote = s.recvfrom(65565)

    traduzido = struct.unpack('!BBHHHBBH4s4s', pacote[0][0:20])

    print 'From:', pacote[1][0]
    print 'Pacote:', traduzido
    print 'IP Version:', traduzido[0] >> 4
    print 'TTL:', traduzido[5]
    print 'Protocol:', traduzido[6]
    print 'Source IP:', socket.inet_ntoa(traduzido[8])
    print 'Target IP:', socket.inet_ntoa(traduzido[9])
    print pacote[0]