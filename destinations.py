
import requests
import json
from bs4 import BeautifulSoup

api_base_url = "http://sandbox.holidayiq.com/"
destination_url = "http://sandbox.holidayiq.com/destinations/"
username = "thack"
password = "thack@hiq"
auth_header = 'Basic %s' % (":".join([username,password]).encode('Base64').strip('\r\n'))
headers = {'content-type' : 'application/json', 'Authorization' : auth_header}

def get_api_content(url):
    response = requests.get(url, headers=headers)
    content = json.loads(response.content)
    return content

def get_nextpage_url(content):
    return str(content['_links']['next']['href'])
   
def get_destination_ids(content):
    dest_list = []
    for dest in content['_embedded']['destinations']:
        dest_list.append(dest['id'])
    return dest_list
    

destination_ids = []
content = get_api_content(api_base_url+"destinations")
destination_ids.extend(get_destination_ids(content))
next_page_url = str(content['_links']['next']['href'])

while True:
    content = get_api_content(next_page_url) 
    destination_ids.extend(get_destination_ids(content))
    try:
        next_page_url = str(content['_links']['next']['href'])
    except:    
        break

f = open('workfile', 'wb')
for id in destination_ids:
   content =  get_api_content(destination_url+str(id))
   f.write(str(id)+",")
   description = BeautifulSoup(content['shortDescription']).get_text()
   print description    
   f.write(description.encode('utf-8'))
   f.write("\n")
f.close()
