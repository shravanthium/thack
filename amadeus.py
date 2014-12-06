import requests

#http://api.travelinnovationsandbox.com/v1.2/airports/nearest-relevant?latitude=46.6734&longitude=-71.7412

near_air_url = 'http://api.travelinnovationsandbox.com/v1.2/airports/nearest-relevant'

def get_nearest_airport(latitude,longitude):
    query = "latitude=" + str(latitude) + \
            "&longitude=" + str(longitude)
    url =  near_air_url+"?"+query
    print url
    response = requests.get(url)
    if response.status_code ==200:
        return response.content
    else:
        print "No response"
        return None

print get_nearest_airport(12,75)


    

