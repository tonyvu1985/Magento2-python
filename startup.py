#!/usr/bin/python

class bcolor:
	HEADER = '\033[91m'
	ENDC   = '\033[0m'

print bcolor.HEADER  + '\n======= COMMAND AVAILABLE ======='
data = [['1. chrome', '5. phpstorm', '9. dev55_ssh // dev55_sftp'], ['2. binami_ssh // binami_sftp','6. binami_ssh_magento2 // binami_sftp_magento2','10. TT_ssh // TT_sftp'], ['3. sublime','7. debian8.2_ssh // debian8.2_sftp',''], ['4. soapui','8. netbean', '']]
col_width = max(len(word) for row in data for word in row) + 2 # padding

for row in data:
	print "" . join(word.ljust(col_width) for word in row)

print bcolor.ENDC 
