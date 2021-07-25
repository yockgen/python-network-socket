import socket
import binascii

ETH_P_ALL = 3
interface = 'wlp2s0'


src_mac = "28:c6:3f:f3:c2:9e"
dst_mac = "28:c6:3f:f3:c2:9e"

src = binascii.unhexlify(src_mac.replace(':', ''))
dst = binascii.unhexlify(dst_mac.replace(':', ''))


#dst = b'\x08\x00\x27\xdd\xd7\x43'  # destination MAC address
#src = b'\x08\x00\x27\x8e\x75\x44'  # source MAC address


#proto = b'\x08\x00'                # ethernet frame type
proto = b'\x08\x00'                # ethernet frame type

payload = '!!!!yockgen001!!!!!'.encode()            # payload

iCnt = 0;
while True:
	s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ALL))
	s.bind((interface, 0))

	s.sendall(dst + src + proto + payload)
	s.close()
	iCnt = iCnt + 1
	print('\rSent from %s to %s count %d'% (src_mac,dst_mac,iCnt))
