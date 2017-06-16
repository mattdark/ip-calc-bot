import re
from ipaddress import IPv4Address, IPv4Network, ip_network

def calcip(hosts,net_address):
    classA = IPv4Network(("10.0.0.0", "255.0.0.0"))
    classB = IPv4Network(("172.16.0.0", "255.240.0.0"))
    classC = IPv4Network(("192.168.0.0", "255.255.0.0"))

    m = 0
    n = 2
    b = False
    while not b:
        if (n ** m) >= int(hosts):
            b = True
        m = m + 1

    nh = (2 ** m) - 2
    bits = 32 - (m - 1)
    msk = ('1' * bits) + ('0' * (m-1))
    octect = re.findall('.{1,8}', msk)
    mask = ''

    for i in octect:
        mask += str(int(i, 2)) + '.'
    mask = mask[:-1]

    range = list()
    for x in ip_network(net_address + '/' + str(bits)).hosts():
        range.append(str(x))

    r = range[0] + " - " + range[len(range) - 1]
    return mask, r
