import socket
import struct

ip = input('IP Address: ')
networks = input('Enter the Hosts separated with comma: ').split(',')


def powerFinder(hosts):
    for n in range(50):
        if (pow(2, n) - 2) >= int(hosts):
            return n


def cidr_to_netmask(cidr):
    net, net_bits = cidr.split('/')
    host_bits = 32 - int(net_bits)
    netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
    return net, netmask


for network in networks:
    ip_parts = ip.split('.')
    ip_parts = [int(part) for part in ip_parts]
    N = powerFinder(network)
    print("=" * 60)
    print(f"\nResult for {ip} with {network} hosts")
    print(f"Number of hosts\t= {network}")
    print(f"(2^n)-2\t>= {network}")
    print(f"N\t= {N}")
    print(f"2^n\t= {pow(2, N)}")
    for n in range(1, 33):
        if n > 32 - N:
            print('0', end='')
        else:
            print('1', end='')
        if n == 32:
            pass
        elif n % 8 == 0:
            print('.', end='')
    print(f"\nSubnet Mask Length\t= 32 - {N} = {32 - N}")
    print(f"Subnet Mask Value\t= {cidr_to_netmask(ip + '/' + str(32 - N))[1]}")
    print(f"Network Address\t= {ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.{ip_parts[3]} / {32 - N}")
    for host in range(1):
        ip_parts[3] = ip_parts[3] + 1
        if ip_parts[3] % 256 == 0:
            ip_parts[2] = ip_parts[2] + 1
            ip_parts[3] = 1
    print(f"First Valid Host Address\t= {ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.{ip_parts[3]}")
    for host in range(2, pow(2, N)):

        if ip_parts[3] % 256 == 0:
            ip_parts[2] = ip_parts[2] + 1
            ip_parts[3] = 0

        ip_parts[3] = ip_parts[3] + 1

    print(f"Last Valid Host Address\t= {ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.{ip_parts[3] - 1}")
    print(f"Broadcast Address\t= {ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.{ip_parts[3]}")
    ip_parts[3] = ip_parts[3] + 1
    if ip_parts[3] % 256 == 0:
        ip_parts[2] = ip_parts[2] + 1
        ip_parts[3] = 0
    ip = ".".join([str(part) for part in ip_parts])