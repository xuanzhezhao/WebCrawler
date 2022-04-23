from unittest import result
import requests
from dem12 import get_dem_link
import argparse				#导入区域名


parser = argparse.ArgumentParser()	
parser.add_argument('--region_name', type=str, default="download")
args = parser.parse_args()
region_name = args.region_name
######  Params of Interface1 #######
headers = {
    'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',
}

params = (
    ('intersectsWith', 'POLYGON((96.0005 43.9981,96 43.9981,96 44,90 44,90 40,96 40,96 43.1682,96.0006 43.1678,96.0005 43.9981))'),
    ('platform', 'ALOS'),
    ('instrument', 'PALSAR'),
    ('start', '2006-05-15T16:00:00Z'),
    ('end', '2011-04-22T15:59:59Z'),
    ('processinglevel', 'RTC_HI_RES'),
    ('beamSwath', 'DSN,FBS,FBD,PLR,WB1,WB2'),
    ('maxResults', '50000'),
    ('output', 'jsonlite2'),
)

s = requests.session()
s.keep_alive = False
requests.adapters.DEFAULT_RETRIES = 7

response1 = s.get('https://api.daac.asf.alaska.edu/services/search/param', headers=headers, params=params)

##############  END  ###############

state1 = response1.json()

results = state1["results"]

fn = []
resource_link = []

for iter in results :
    #print(iter['fn'])
    fn.append(iter['fn'])
    link = "https://unzip.asf.alaska.edu/RTC_HI_RES/A3/" + iter['fn']
    resource_link.append(link)
    #print(link)
print(len(results))

#download:https://unzip.asf.alaska.edu/RTC_HI_RES/A3/AP_21641_FBS_F0770_RT1.zip
"""
with open('response1.json', 'w', encoding='utf-8') as json_file:
   json.dump(state1, json_file, ensure_ascii=False)
   print("write json file success!")

"""
####### Params of interface2: ########
cookies = {
    '_gid':'GA1.2.1383433462.1650618216', 
    'cebs':'1', 
    '_ce.s': 'v~6e8392fbcd33749ff56816cb83bba69fc5680bc0~vpv~2~v11.rlc~1650618221280~v11slnt~1650008119225',
    'asf-urs':'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJmaXJzdF9uYW1lIjoid19oMTYzLmNvbSIsImxhc3RfbmFtZSI6IndhbmdodWEiLCJ1cnMtdXNlci1pZCI6IndfaDE2My5jb20iLCJ1cnMtYWNjZXNzLXRva2VuIjoiZXlKMGVYQWlPaUpLVjFRaUxDSnZjbWxuYVc0aU9pSkZZWEowYUdSaGRHRWdURzluYVc0aUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5SjBlWEJsSWpvaVQwRjFkR2dpTENKamJHbGxiblJmYVdRaU9pSkNUMTl1TjI1VVNXeE5iR3BrZGxVMmExSlNRak5uSWl3aVpYaHdJam94TmpVek1qRXhPVGd6TENKcFlYUWlPakUyTlRBMk1UazVPRE1zSW1semN5STZJa1ZoY25Sb1pHRjBZU0JNYjJkcGJpSXNJblZwWkNJNkluZGZhREUyTXk1amIyMGlmUS5QYjRUV3lHb0lyWlQ4X09HYnRMS1gtUTd1RV9ENW5MdlVUbkZib1VqMGlFIiwidXJzLWdyb3VwcyI6W10sImlhdCI6MTY1MDYxOTk4MywiZXhwIjoxNjUxMjI0NzgzfQ.gmkrZ1WpEPoi-B4bFoRlFXMJSCQcQv0BTH80YUc-l8LS9HN0rf7sV8srhku02KeApqLz6CkGifbtqS2K6wgWnRRiT2_t2pBL7M5ByDG8Q7BCk6U2o1PzXlZoU3IJrubyr7X1wMkxc2Z1s5aOkGf35fiGPXyyvu8UyikXq1mbf0NIG6lge8gglf4b2Xs8VJfr1rUBPgm6FEk15La-iC1BxhwSeor0ZpLqCYGcI__YWzSk2G3PcP0b6j7zEAeSi1_ouTCXSZ889ly-VjHH22PV2nxKPtk-1Msixu7XrROd8tGKbbE8zMT6aMguLEWQM0tOAMLomLOY6AahVFF2dtm3-sSqEdR5DBqxM6DQUmkOsYi-2AHGuTmdbjgZVloCP43DZEJsUZL7PWcsM9jw0f9lKOfMJn9Y9_mhrKZmXSef8WG8Yu72KWoNM3suyErD_5usFKReXXpM3JazJH6bQ4-e6Wr_p7R0IG6fAiitqJsh8z60gO3C2xO2QZ48DA2iKbXbSrCWY1ULBZedgOG3j60bOgFzX9I7iwFoqXOOc_OQIXM-naNQaw8WAAD00ilRNse29lsy80Zl9iwtqZX8xPa8K0eQqwevjj0uGZIBsirlq_RXrgFiNbys3uBV16BLg9_etqzCtH4Ba4jiH6zFANKw14jkNesP1lZP04QOxHm4v7o; urs-user-id=w_h163.com; urs-access-token=eyJ0eXAiOiJKV1QiLCJvcmlnaW4iOiJFYXJ0aGRhdGEgTG9naW4iLCJhbGciOiJIUzI1NiJ9.eyJ0eXBlIjoiT0F1dGgiLCJjbGllbnRfaWQiOiJCT19uN25USWxNbGpkdlU2a1JSQjNnIiwiZXhwIjoxNjUzMjExOTgzLCJpYXQiOjE2NTA2MTk5ODMsImlzcyI6IkVhcnRoZGF0YSBMb2dpbiIsInVpZCI6IndfaDE2My5jb20ifQ.Pb4TWyGoIrZT8_OGbtLKX-Q7uE_D5nLvUTnFboUj0iE',
    '_ga': 'GA1.2.59271381.1648803793',
    '_gat_UA-991100-5': '1',
}
headers = {'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',}

########### END ##########

dem_link_source = []
count = 1
num = len(resource_link)
for link in resource_link:
    dem_link = get_dem_link(link,headers=headers, cookies=cookies)
    dem_link = link + "/" + dem_link
    dem_link_source.append(dem_link)
    print(count,"of", num)
    count = count+1
"""
dem_link_jsonsource = json.dumps(dem_link_source)
with open("json_dem_file/dem_download.json", 'w', encoding='utf-8') as json_file:
        json.dump(dem_link_jsonsource, json_file, ensure_ascii=False)
        print(" write downlaod json file success!")
"""
filename = open('dem_file/'+region_name+'_url.txt', 'w')
for value in dem_link_source:
    filename.write(str(value))
    filename.write('\n')
filename.close()








    


#print(state)
# https://search.asf.alaska.edu/#/?zoom=4.394&center=107.728,20.618&dataset=ALOS&resultsLoaded=true&granule=ALPSRP158060380-RTC_HI_RES&start=2006-05-15T16:00:00Z&end=2011-04-22T15:59:59Z&polygon=POLYGON((110%2018.3333,110.5%2018.3333,110.5%2018.6667,111%2018.6667,111%2019.3333,111.5%2019.3333,111.5%2020,109%2020,109%2019.6667,108.5%2019.6667,108.5%2018.3333,109%2018.3333,109%2018,110%2018,110%2018.3333))&beamModes=DSN,FBS,FBD,PLR,WB1,WB2&productTypes=RTC_HI_RES