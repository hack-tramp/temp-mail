#!/usr/bin/python
# -*- coding: utf-8 -*-
#API docs here: https://temp-mail.org/en/api/

import requests, hashlib
session = requests.Session() 

name = 'test1n9'

#only create new email if one wasnt provided
if name.find('@')==-1:
   #going with the first by default
   domain_choice = 0
   getres = session.get('https://api4.temp-mail.org/request/domains/format/json')
   jsonres = getres.json()
   print('domains available:')
   for domain in jsonres:
      print(domain)
   print('choosing domain number '+str(domain_choice))
   name = name + str(jsonres[domain_choice])
   
md5hash = hashlib.md5(name.encode('utf-8')).hexdigest()
#print(md5hash)

#get emails (if no emails response will be 'error')

#omit /format/json/ for xml response 
getres = session.get('https://api4.temp-mail.org/request/mail/id/'+md5hash+'/format/json/')
jsonres = getres.json()
print('emails recd:')
for em in jsonres:
   print(em)
   
#delete email - requires mail_id from json res obj - response should be 'success'

#mail_id = ''
#getres = session.get('https://api4.temp-mail.org/request/delete/id/'+mail_id+'/')
#print(getres.text)
