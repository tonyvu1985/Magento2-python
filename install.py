#!/usr/bin/python
import os
import sys
# require to install MySQLdb module
# also need to install setuptools module, sudo apt-get install python-dev, sudo apt-get install libmysqlclient-dev
import MySQLdb 

#print 'Number of arguments: ', str(sys.argv)
arg = sys.argv
#print 'argument1: ', arg[1]
#print 'argument2: ', arg[2]

# create connection 
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="human01", db="test")

# prepare a cursor object using cursor() method
cursor = conn.cursor()

#check if Temando extension is install 
cursor.execute("SELECT * FROM setup_module WHERE module='Temando_Temando'")
conn.commit()
data = cursor.fetchall()
for row in data:
    print row

sys.exit()

# copy Magento 2 extension to destination directory: app / code
# arg[1]: Magento 2 extension
# arg[2]: Magento root directory
cpCmd = 'cp -a ' + str(arg[1]) +  ' ' + str(arg[2]) + 'app/code'
#print 'cmd ', cmd
#cmd = 'l' 's'
os.system(cpCmd)

# run command to upgrade Magento 2 extension 
upgradeCmd = 'php' + str(arg[2]) + 'bin/magento setup:upgrade'
os.system(upgradeCmd)

# clean all Magento cache: cache, generation and page_cache folder
cleanCmd = 'rm -rf'  + str(arg[2]) + 'var/cache' + ' ' + str(arg[2]) + ' ' + 'var/generation' + ' ' + str[arg[2]] + ' ' + 'var/page_cache';
