
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from requests.models import Response

####Request####
Take_html=requests.get(f'https://www.openstreetmap.org/api/0.6/changeset/{95969191}/download')
# print(Take_html.headers['Content-Type'])# to know xml or json
'''
***** Take value you wanted base on requests *xml from web***
'''
a=Take_html.content 

root=ET.fromstring(a)
#ET.dump(root) #show all xml file
'''
1. The first way
'''
list=[]
for child in root.iter('way'): # iter is a iteration find 'way'
    # print(child.tag)
    atrribute=child.attrib
    list.append(atrribute['id'])
print(list)

'''
2. The second way
'''
way2=[]
for child01 in root.findall('create'):
    # print(child01)
    way1=child01.find('way')
    if way1!=None:
        att=way1.attrib
        way2.append(att['id'])
print(way2)

'''
***** Take value you wanted from web using BeautifulSoup***
'''

Soup=BeautifulSoup(Take_html.text,features='html.parser')
Ways=Soup.find_all('way')
List_ways_id=[]
for Ways_id in Ways:
    List_ways_id.append(Ways_id['id'])
print(List_ways_id)
