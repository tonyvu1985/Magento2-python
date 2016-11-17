#!/usr/bin/python

class bcolor:
    TEXT = '\033[95m'
    ENDC = '\033[0m'

import os
import sys
# require to install MySQLdb module
# also need to install setuptools module, sudo apt-get install python-dev, sudo apt-get install libmysqlclient-dev
import MySQLdb 
import time

# helper
if (len(sys.argv) <= 1):
    print bcolor.TEXT + '=== INSTRUCTION OF HOW TO USE SCRIPT ===' + bcolor.ENDC
    print "1. Type in Terminal: python install.py [pathToExtension] [pathToMagentoWebroot]"
    print "2. DONE"
    sys.exit()


#print 'Number of arguments: ', str(sys.argv)
arg = sys.argv
extension = arg[1]
webroot = arg[2]

# create connection 
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="human01", db="totaltool")

# prepare a cursor object using cursor() method
cursor = conn.cursor()

#check if Temando extension is install 
cursor.execute("SELECT * FROM setup_module WHERE module='Temando_Temando'")
data = cursor.fetchall()
if data:
    try:
        # remove all Temando extension 
        print "remove a existing Temando extenion..."
        time.sleep(2)        
        rmCmd = 'rm -rf ' + webroot + 'app/code/Temando'
        os.system(rmCmd)

        # remove temando tables
        print "remove old temando tables..."
        time.sleep(2)        
        cursor.execute("DROP TABLE IF EXISTS `temando_booking`,`temando_box`,`temando_carrier`,`temando_origin`,`temando_quote`,`temando_shipment`,`temando_shipment_item`,`temando_zone`");

        # remove all temando configuration 
        cursor.execute("DELETE FROM core_config_data WHERE path like '%temando%'")
        
        # remove temando setup_module
        print "remove temando configuration..."
        time.sleep(2)        
        cursor.execute("DELETE FROM setup_module WHERE module like '%Temando%'")
        conn.commit()

    except MySQLdb.Warning, e:
        print str(e) 

# copy Magento 2 extension to destination directory: app / code
print "copy new temando extension..."
time.sleep(2)
cpCmd = 'cp -a ' +  extension +  ' ' + webroot + 'app/code'
#print 'cmd ', cmd
os.system(cpCmd)

# run command to upgrade Magento 2 extension 
print "run magento upgrade..."
time.sleep(2)
upgradeCmd = 'php ' + webroot + 'bin/magento setup:upgrade'
os.system(upgradeCmd)

# clean all Magento cache: cache, generation and page_cache folder
print "Magento cache cleaning..."
time.sleep(2)
cleanCmd = 'rm -rf '  + webroot + 'var/cache' + ' ' + webroot + 'var/generation' + ' ' + webroot + 'var/page_cache'
os.system(cleanCmd)

# generate magento static content
print "magento static content generate..."
time.sleep(2)
generateCmd = 'php ' + webroot + 'bin/magento setup:static-content:deploy'
os.system(generateCmd)

# generate magento static content
print "set permission for var and pub/static..."
time.sleep(2)
generateCmd = 'chmod -R 777 ' + webroot + 'var/cache' + ' ' + webroot + 'var/generation' + ' ' + webroot + 'var/page_cache' + ' ' + webroot + 'pub/static'
os.system(generateCmd)

# complete 
print "COMPLETED..."
