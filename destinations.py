
import requests
import json

api_base_url = "http://sandbox.holidayiq.com/"
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
    
content = get_api_content(api_base_url+"destinations")
next_page_url = str(content['_links']['next']['href'])

while True:
    content = get_api_content(next_page_url) 
    next_page_url = str(content['_links']['next']['href'])
    print next_page_url

    if next_page_url == None:
        break

