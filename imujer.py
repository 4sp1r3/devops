import dns.resolver
import requests


#Get A records from imujer.com
answers = dns.resolver.query('www.imujer.com', 'A')

# For each 
for rawdata in answers:
    # get uri
    uri = 'http://199.34.125.35/test?email=me%40gmail.com&record=' + str(rawdata)
    
    #perform request
    r = requests.get(uri)
    
    #print results
    print ('Request: %s -> Response: %s') % (uri, r.status_code)
