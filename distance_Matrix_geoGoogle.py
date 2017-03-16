import urllib
import json

serviceurl = 'https://maps.googleapis.com/maps/api/distancematrix/json?'


while True:
    origin = raw_input('Enter Origin: ')
    if len(origin) < 1 : break
    destination = raw_input('Enter Destination: ')
    mode = raw_input('Enter Mode ( "driving" or "walking"): ')

    url = serviceurl + urllib.urlencode({'sensor':'false', 'origins': origin, 'destinations': destination, 'mode': mode})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    #print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    #print json.dumps(js, indent=4)

    duration = js["rows"][0]["elements"][0]["duration"]["text"]
    distance = js["rows"][0]["elements"][0]["distance"]["text"]
    print 'Duration',duration,'\n''Distance',distance
    ori = js['origin_addresses'][0]
    des = js['destination_addresses'][0]
    print ori , "     TO     ", des
