def checkIPs():
    counter = 0
    matches = 0

    with open('forti_leaked_ips.txt', 'r') as infile:
        
        for line in infile:
            counter += 1
            port_removed = line.split(':')[0]
            ips_to_test = open('ips_to_check.txt', 'r')
            for entry in ips_to_test:
                if entry.strip() == port_removed.strip():
                    
                    print('**Match found: ' + entry + '**********')
                    matches += 1
            ips_to_test.close()
    print('Tested ' + str(counter) + ' Addresses')
    print('Found ' + str(matches) + ' matches!')

checkIPs()
    
    