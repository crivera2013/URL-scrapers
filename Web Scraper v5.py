# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 10:17:03 2016

@author: crivera
"""
import re
import json
import time
from bs4 import BeautifulSoup
import requests
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

# suppression list of generic websites
# some companies don't have websites or are too small and so generic websites pop up as 
suppression = ['www.bbb.org','www.usbiz.org','www.angieslist.com','www.yellowpages.com',
              'www.care.com','localbiziness.com','www.manta.com','www.buzzfile.com',
              'www.bloomberg.com','www.unitedstatesbusinessonline.com','www.businessdatabase.us',
              'www.linkedin.com','enterprisesgeorgia.com','www.biztoolsone.com','www.facebook.com',
              'www.b2byellowpages.com','www.manta.com','en.wikipedia.org','listings.findthecompany.com',
              'www.ic.gc.ca','www.yellowpages.ca','www.healthgrades.com','yelp.com','health.usnews.com',
              'healthgrades.com','www.greatschools.org','nursing-homes-healthgrove.com','www.indeed.com',
              'greatschools.org','www.privateschoolreview.com','www.caring.com','www.allonesearch.com',
              'listings.ftb-companies-ca.com','www.collegereview.com','www.wellness.com','www.bizjournals.com','fail',
              'nursing-homes.healthgrove.com','webcache.googleusercontent.com','listings.fta-companies-ca.com',
              'cacompanylist.com','www.canpages.ca','www.yelp.com','www.smallbusinessdb.com','www.vitals.com',
              'private-schools.startclass.com','localtown.us','businessbay.us','localtown.us',
              'businessbay.us','childcarecenter.us','doctor.webmd.com','yellowpages.ca',
              'www.glassdoor.com','nursing-homes.healthgrove.com','oyp.us','www.superpages.com','ca.linkedin.com',
              'smallbusinessdb.com','affordablehousingonline.com','www.schoolfamily.com','www.whitepages.com',
              'k12.niche.com','www.trulia.com','canadageo.com','www.michigantownships.org','www.profilecanada.com',
              'www.tuugo.me','www.toronto.ca','ca.indeed.com','start.cortera.com','www.crunchbase.com','www.policeone.com',
              'georgia.gov','www.nytimes.com','www.zillow.com','businessfinder.al.com','indeed.com','www.companylisting.ca',
              'www.mycollegeoptions.org','www.publicschoolreview.com','www.quicktransportsolutions.com','411.ca',
              'www.edline.net','www.michigan.gov','automotiveoem.com','bizjournals.com','www.collegeview.com',
              'www.desjardins.com','www.legacy.com','www.nexdu.com','www.oregon.gov','www.ourparents.com',
              'www.prnewswire.com','www.salespider.com','www.transportservices.info','www.usaypage.com',
              'businessfinder.syracuse.com','www.albertahealthservices.ca','www.bizapedia.com','www.city-data.com',
              'www1.toronto.ca','broadbandnow.com','librarytechnology.org','search.211north.ca','sites.google.com',
              'www.firedepartment.net','www.homehealthcareagencies.com','www.mapquest.com','www.monster.com','www.realtor.com',
              'www2.gnb.ca','allonesearch.com','crunchbase.com','glassdoor.com','mental-health-facilities.healthgrove.com',
              'ntip.gov.nu.ca','privateschoolreview.com','schools.nyc.gov','www.businesswire.com','www.cbdc.ca',
              'www.maxpreps.com','www.radiologyimagingcenters.com','www.rootsweb.ancestry.com','www1.gnb.ca',
              'addresscustomerservicecenternumber.com','alabama.uscofinder.com','nunavuttourism.com','quicktransportsolutions.com',
              'schoolfamily.com','usfiredept.com','www.cincinnati-oh.gov','www.coldwellbanker.com','www.corporationwiki.com',
              'www.electricpower.cc','www.healthpei.ca','www.ibegin.com','www.in.gov','www.ok.gov','www.pagesjaunes.ca',
              'www.presswork.cc','www.saskatchewan-businessdirectory.com','www.sedar.com','www.seniorhousingnet.com','www.servicecanada.gc.ca',
              'www.thomasnet.com','www.tripadvisor.com','www.uslocaldir.com']


###########################################################################
def google(rawCompany, proxy, useragent):

    # get rid of generic words and code breaking characters like '&;
    rawCompany = rawCompany.replace("group","")
    rawCompany = rawCompany.replace(".","")
    rawCompany = rawCompany.replace("&","")
    rawCompany = rawCompany.replace("  "," ")
    rawCompany = rawCompany.replace("'","")
    rawCompany = rawCompany.replace(" ","+")
    
    # set up fake IP address for web request
    # append the input company name to the url address
    # google search: company home page 'input company'
    url ="https://www.google.com/search?q=" + rawCompany
    page = requests.get(url,proxies=proxy, headers=useragent)
    
    # read webpage as 'lxml' 
    soup = BeautifulSoup(page.content, 'lxml')
    # grabs the first html address from the first result that comes up
    fire = soup.find_all("h3",{"class":"r"})
    tree = fire[0].find_all("a")
    z = tree[0]['href']
    print z
    
    tree = fire[1].find_all("a")
    a = tree[0]['href']
    #print "google"
    #print rawCompany    
    #print z
    #print a
    #print "###########"
    time.sleep(1)
    #set sleep timer to not overload google server and get booted.
    #return web address for company
    return z,a
    
############### end of google function
 ############################################################################
    
    
#########################

def bing(rawCompany, proxy, useragent):

    # get rid of generic words and code breaking characters like '&;
    rawCompany = rawCompany.replace("group","")
    rawCompany = rawCompany.replace(".","")
    rawCompany = rawCompany.replace("&","")
    rawCompany = rawCompany.replace("  "," ")
    rawCompany = rawCompany.replace("'","")
    rawCompany = rawCompany.replace(" ","+")
    
    # set up fake IP address for web request
    # append the input company name to the url address
    # google search: company home page 'input company'
    url ="http://www.bing.com/search?q=company%20home%20page" + rawCompany
    page = requests.get(url)
    
    # read webpage as 'lxml' 
    soup = BeautifulSoup(page.content, 'lxml')
    # grabs the first html address from the first result that comes up
    fire = soup.find_all("li",{"class":"b_algo"})
    #print fire[1]
    tree = fire[0].find_all("a")
    z = tree[0]['href']

    tree = fire[1].find_all("a")
    a = tree[0]['href']
    
    #print "bing"
    #print rawCompany     
    #print z    
    #print a
    #print "###########"
    time.sleep(1)
    #set sleep timer to not overload google server and get booted.
    #return web address for company
    return z,a
    
############### end of Bing function
 ############################################################################   

#######################
def Duck(rawCompany, proxy, useragent):
    rawCompany = rawCompany.replace("group","")
    rawCompany = rawCompany.replace(".","")
    rawCompany = rawCompany.replace("&","")
    rawCompany = rawCompany.replace("  "," ")
    rawCompany = rawCompany.replace("'","")
    rawCompany = rawCompany.replace(" ","%20")

    url ="https://duckduckgo.com/html/?q=company%20home%20page%20"+rawCompany
    page = requests.get(url, proxies = proxy, headers = useragent)

    soup = BeautifulSoup(page.content, 'lxml')

    fire = soup.find_all("div",{"class":"result results_links results_links_deep web-result "})

    tree = fire[0].find_all("a")
    z = tree[0]['href']

    tree = fire[1].find_all("a")
    a = tree[0]['href']
    #print "DUck Duck Go"
    #print rawCompany     
    #print z
    #print a
    #print "#############"
    time.sleep(1)
    return z, a

#################### End of Duck Duck Go function
##############################################################################

###### ask.com function

def Ask(rawCompany,useragent):
    
    rawCompany = rawCompany.replace("group","")
    rawCompany = rawCompany.replace(".","")
    rawCompany = rawCompany.replace("&","")
    rawCompany = rawCompany.replace("  "," ")
    rawCompany = rawCompany.replace("'","")
    rawCompany = rawCompany.replace(" ","+")
    
    url ="http://www.ask.com/web?q=company+home+page+" + rawCompany
    
    page = requests.get(url,headers=useragent)
#    # read webpage as 'lxml' 
    soup = BeautifulSoup(page.content, 'lxml')
    
    fire = soup.find_all("div",{"class":"web-result ur tsrc_tled "})

    water = str(fire[0].p).split(">")
    water = water[1].split("/")
    z = water[0]

    water = str(fire[1].p).split(">")
    water = water[1].split("/")
    a = water[0]
    #print "ASK JEEVES"
    #print rawCompany     
    #print z
    #print a
    #print "##########"
    time.sleep(1)
    return z, a
    
##############################################################################
    
#### yandex function
    
def Yandex(rawCompany,useragent,proxy):
    rawCompany = rawCompany.replace("group","")
    rawCompany = rawCompany.replace(".","")
    rawCompany = rawCompany.replace("&","")
    rawCompany = rawCompany.replace("  "," ")
    rawCompany = rawCompany.replace("'","")
    rawCompany = rawCompany.replace(" ","%20")

    url ="https://www.yandex.com/search/?text=company%20home%20page%20"+rawCompany
    page = requests.get(url, proxies = proxy, headers = useragent)

    soup = BeautifulSoup(page.content, 'lxml')
    
    fire = soup.find_all("li",{"data-cid":"0"})
    water = fire[0].find_all("a",{"class":"link link_outer_yes path__item"})
    z = water[0]['href']
    
    fire = soup.find_all("li",{"data-cid":"1"})
    water = fire[0].find_all("a",{"class":"link link_outer_yes path__item"})
    a = water[0]['href']
    
    #print "YANDEX"
    #print rawCompany 
    #print z
    #print a
    #print "##############"
    time.sleep(1)
    return z, a

##### end of Yanex function

### IXQuick function

def IXQuick(rawCompany,useragent,proxy):
    rawCompany = rawCompany.replace("group","")
    rawCompany = rawCompany.replace(".","")
    rawCompany = rawCompany.replace("&","")
    rawCompany = rawCompany.replace("  "," ")
    rawCompany = rawCompany.replace("'","")
    rawCompany = rawCompany.replace(" ","+")

    url ="https://www.ixquick.com/do/dsearch?pl=opensearch&language=english&query=company+home+page+"+rawCompany
    page = requests.get(url, proxies = proxy, headers = useragent)

    soup = BeautifulSoup(page.content, 'lxml')
    
    fire = soup.find_all("li",{"id":"result1"})
    water = fire[0].find_all("span",{"class":"url"})
    x = str(water[0]).split(">")
    y = x[1].split("<")
    z = y[0]
    

    fire = soup.find_all("li",{"id":"result2"})
    water = fire[0].find_all("span",{"class":"url"})
    x = str(water[0]).split(">")
    y = x[1].split("<")
    a = y[0]
    
    #print "IXQUICK"
    #print rawCompany 
    #print z
    #print a
    #print "############"
    time.sleep(1)
    return z, a
#########################################################    
    
####################### proxy discover and check functions
def proxiesGet():
    url = # call to a ip proxy api goes here'
    url = url + 'limit1&country_code=US'
    test = requests.get(url)
    fire = json.loads(test.content)
    water = fire['data']
    earth = water['proxies']
    air = earth[0]
    light = air['ip']
    
    good_proxies = {'http':'http://'+light}
    
    return good_proxies

# check if the proxy is good
def checkFake(proxy):  
    fire = proxy
    url ="http://www.bing.com/search?q=if you give a mouse a cookie"
    page = requests.get(url,proxies=fire)
    soup = BeautifulSoup(page.content, 'lxml')
    fire = soup.find_all("li",{"class":"b_algo"})
    if len(fire) > 0:
    	print 'worked'
        return True
    else: 
        return False
#############################################

def urlSplitter(web, web2):
    web = web.split("/") 
    #web[2] removes the 'http://' and any portion of string after 'com'
    #print web[2]
    web = web[2]    
    if web in suppression:
        web = ''
    if 'webcache' in web:
        web = ''
            
    web2 = web2.split("/")
    #print web2[2]
    web2 = web2[2]
    if web2 in suppression:
        web2 = ''
    if 'webcache' in web2:
        web2 = ''
        
    return web, web2
############################################

#creates pop up window to select the input file        
from Tkinter import Tk
from tkFileDialog import askopenfilename
Tk().withdraw()
filename = askopenfilename()

import xlrd
workbook = xlrd.open_workbook(filename)
workbook = xlrd.open_workbook(filename, on_demand = True)
worksheet = workbook.sheet_by_index(0)
first_row = [] # The row where we stock the name of the column
for col in range(worksheet.ncols):
    first_row.append( worksheet.cell_value(0,col) )
# transform the workbook to a list of dictionaries
data =[]
counter = 0
for row in range(1, worksheet.nrows):
    elm = {}
    for col in range(worksheet.ncols):
        elm[first_row[col]]=worksheet.cell_value(row,col)
    counter = counter + 1
    print counter
    data.append(elm)


#convert dictionary into utf-8 format
holder = []
for mydict in data:
     holder.append( {unicode(k).encode("utf-8"): unicode(v).encode("utf-8") for k,v in mydict.iteritems()} )
print "unicode?"
data = holder
##################
companies = []
for i in data:
	companies.append({'company':i['company']})


# used to create fake useragents for url requests
from fake_useragent import UserAgent
ua = UserAgent()
 

outputCompanies = [] 
x = 0
counter = 0

print "number of companies"
print len(companies)


for i in companies:
    if x % 25 == 0:
        print "new AGENTS"
        useragent = ua.chrome
        useragent = {"user-agent":useragent}
        print useragent
        proxy = proxiesGet()
        print proxy
        #while checkFake(proxy) == False:
         #   print "proxy fail"
          #  time.sleep(2)
           # proxy = proxiesGet()
    
    
    if x % 5 == 0:
        try:
            #send company name, fake proxy, and fake header to google function
            web, web2 = google(i['company'],proxy,useragent)
            # 'web' is a web address
            z, a = urlSplitter(web, web2)
            counter = counter + 1
            print counter
            #print z
            #print a
            outputCompanies.append({'company':i['company'], 'url':z,'url2':a})
            z = "fail"
            a = "fail"
        except:
            pass
    
    if x % 5 == 1:
        try:
            #send company name, fake proxy, and fake header to google function
            web, web2 = bing(i['company'],proxy,useragent)
            # 'web' is a web address
            b, d = urlSplitter(web, web2)
            counter = counter + 1
            print counter
            #print b
            #print d
            outputCompanies.append({'company':i['company'], 'url':b,'url2':d})
            b = "fail"
            d = "fail"
        except:
            pass

    if x % 4 == 2:
        try:
            #send company name, fake proxy, and fake header to google function
            z, a = Duck(i['company'],useragent)
            # 'web' is a web address
            z, a = urlSplitter(web, web2)
            counter = counter + 1
            print counter
            print z
            print a
            outputCompanies.append({'company':i['company'], 'url':z,'url2':a})
        except:
            pass

    if x % 5 == 2:
        try:
            e,f = Ask(i['company'],useragent)
            counter = counter + 1
            print counter
            #print e
            #print f
            outputCompanies.append({'company':i['company'], 'url':e,'url2':f})
            #e = "fail"
            #f = "fail"
        except:
            pass
    
    if x % 5 == 3:
        try:
            #send company name, fake proxy, and fake header to google function
            web, web2 = Yandex(i['company'],proxy,useragent)
            # 'web' is a web address
            g, h = urlSplitter(web, web2)
            counter = counter + 1
            print counter
            #print g
            #print h
            outputCompanies.append({'company':i['company'], 'url':g,'url2':h})
            g = "fail"
            h = "fail"
        except:
            pass
    
    if x % 5 == 4:
        try:
            #send company name, fake proxy, and fake header to google function
            i, j = IXQuick(i['company'],proxy,useragent)
            # 'web' is a web address
            #z, a = urlSplitter(web, web2)
            counter = counter + 1
            print counter
            #print i
            #print j
            outputCompanies.append({'company':i['company'], 'url':i,'url2':j})
            i = "fail"
            j = "fail"
        except:
            pass

    x = x +1

print outputCompanies

# fuzzy match score comparison section
from fuzzywuzzy import fuzz

for i in outputCompanies:
    i['fuzzyScore1'] = fuzz.partial_ratio(i['company'].lower(), i['url'])
    i['fuzzyScore2'] = fuzz.partial_ratio(i['company'].lower(), i['url2'])
    i['good'] = False

data = outputCompanies
outputCompanies = []
for i in data:
    i['TrueURL'] = i['url']
    if i['fuzzyScore2'] > i['fuzzyScore1']:
        i['TrueURL'] = i['url2']


for i in data:
    if i['TrueURL'] != '':
        outputCompanies.append({'company':i['company'],'url':i['TrueURL']}) 

print "####################"

#send to excel file
import xlsxwriter
wb = xlsxwriter.Workbook("HPE output.xlsx")
number_format = wb.add_format({'num_format':'0'})
ws=wb.add_worksheet("output data") 

ordered_list = ['company','url']

first_row=0
for header in ordered_list:
    col=ordered_list.index(header) # we are keeping order.
    ws.write(first_row,col,header) # we have written first row which is the header of worksheet also.

row=1
for player in outputCompanies:
    for _key,_value in player.items():
        col=ordered_list.index(_key)
        ws.write(row,col,_value)
    row+=1

wb.close()
print "webAddressFinder is finished"
