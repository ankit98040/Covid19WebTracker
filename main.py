#pip install plyer
#pip install bs4
#run these two lines on command prompt
#CODE BY: ANKIT PRAMANIK

from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
	notification.notify(
		title = title,
		message= message,
		app_icon= None,
		#app_icon = "C:/Users/ANKIT/Desktop/Python/COVID19/icon.ico",
		timeout = 6
		)

def getdata(url):
	r = requests.get(url)
	return r.text



if __name__== "__main__":
    #while True:
		#notifyMe("ankit", "lets stop this")
	myHtmlData = getdata('https://www.mohfw.gov.in')

		#print(myHtmlData)
	soup = BeautifulSoup(myHtmlData, 'html.parser')
		#print(soup.prettify())

	myDataStr = ""
	for tr in soup.find_all('tbody')[0].find_all('tr'):
			myDataStr += tr.get_text()
	myDataStr = myDataStr[0:]
		#print(myDataStr.split("\n\n"))
	itemlist = myDataStr.split("\n\n")

	states = ['Gujarat','Maharashtra', 'Delhi', 'Tamil Nadu', 'West Bengal']

	for item in itemlist[0:29]:
		datalist = item.split('\n')
		if datalist[1] in states:
			print(datalist)
			ntitile = 'Cases of COVID-19'
			ntext = f"STATE: {datalist[1]}\nTotal: {datalist[2]}\nDeath: {datalist[3]}\nCured: {datalist[4]}"
			notifyMe(ntitile, ntext)
			time.sleep(2)
	time.sleep(36)