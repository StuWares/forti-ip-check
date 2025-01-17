import ipaddress

cidr_range = '20.26.156.215'

ip_list = [str(ip) for ip in ipaddress.IPv4Network(cidr_range)]

for line in ip_list:
    with open('ips_to_check.txt', 'a') as f:
        f.write(line + '\n')