from scapy.all import Ether
from scapy.all import IP
from scapy.all import TCP
from scapy.all import sr1
# tcp_pkt = Ether()/IP()/TCP()

ip = IP(src="127.0.0.1",dst="192.168.0.1")
tcp = TCP(dport=8000,flags="S")
tcp_pkt = ip/tcp
ans = sr1(tcp_pkt)
print(ans.summay())


