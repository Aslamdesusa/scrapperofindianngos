# python2

try:
	import pygsheets
except Exception as e:
	raise e


from selenium import webdriver
import time

#importing important files
import requests, json
from bs4 import BeautifulSoup
import unicodecsv as csv

# activate the selenium module for headless browser
# so that the google chrome can run in background
options = webdriver.ChromeOptions()
options.add_argument('headless')


#authorizing and connecting to the sheet name couponScrapper using the jsonfile
#couponScrapper
try: 
	googleCloud = pygsheets.authorize(service_file='cupanRep.json')
	# sheetName = input('Enter the name of workSheet that you have created and gave the access : ')
	workSheet = googleCloud.open('ngo_details').sheet1
except Exception as e:
	url= 'https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html'
	print('''Include the service account file you can watch the tutorial here ({0}) to create service file
			and save it as coupon-scrappr.json 
			Give access to you Worksheet using it email-id
 '''.format(url))


# URL of the website																																																																														 to start scraping data from
START_URL = "http://www.indiangoslist.com/goa-ngos-list/1"

#Function defined to scrape URL of different NGOs from the website
print "scraping links....."
def scrape_ngo_list(page_url, page_no=1):
	
	#Requesting to open the first page.
	page = requests.get(page_url)

	
	#Setting up BS Instance.
	soup = BeautifulSoup(page.content, "html.parser")
	
	#Finding 'h2' tags inside the 'div' tag of of class 'article'.
	ngo_links = soup.find("div", {'class' : "article"}).findAll('h2')

	#Finding all 'a' attributes within the 'h2' tags.
	ngo_links = [tag.findAll('a') for tag in ngo_links]

	#Extracting the 'href' from the 'a' attribute.
	ngo_links = [i[0].get('href').encode('ascii', 'ignore') for i in ngo_links]
	print ("Found {0} links on page number {1}.").format(len(ngo_links), page_no)

	#Joining the elements of ngo_links with '\n'.
	links = "\n".join(ngo_links)
	links = "\n" + links

	#Opening a csv file to store the ngo links.
    links_file = open("ngo_links.csv", "a")

	#Writing the ngo links in a csv file.
	links_file.write("URL")
    links_file.write(links)
    links_file.close()

	current_page_span = soup.findAll('span', {'class': 'current'})[0]
	next_page_a = current_page_span.find_next('a')
	
	#Try statement to handle errors.
	try:
		next_page_link = next_page_a.get('href')
		print next_page_link
		page_no = page_no + 1
		scrape_ngo_list(next_page_link, page_no)
	except:
		pass


def appendRow(row):
	workSheet.append_table(values=row)
	print('row has been saved!')




def csv_url_reader(url_obj):
	print "wait while opening the csv file and fetch data from the link......"
	reader = csv.DictReader(url_obj, delimiter = ',')
	driver = webdriver.Chrome()
	for line in reader:
		url = line["URL"]
		driver = webdriver.Chrome(chrome_options = options)
		driver.get(url)
		time.sleep(2)


		fat = []

		Ngo_name = []
		ngo_name = driver.find_element_by_xpath('//*[@id="tps_slideContainer_4541"]/div/div/div/div/div/div[3]/div[1]/div[2]')
		name = str(ngo_name.text)
		Ngo_name.append(name)
		Ngo_name = '\n'.join(Ngo_name)
		print( "NGO name: {0}" + Ngo_name).format(len(Ngo_name))

		Unique_Id = []
		idCode = driver.find_element_by_xpath('//*[@id="tps_slideContainer_4541"]/div/div/div/div/div/div[3]/div[2]/div[2]')
		idC = str(idCode.text)
		Unique_Id.append(idC)
		Unique_Id = '\n'.join(Unique_Id)
		print("Unique Id of VO/NGO: " + Unique_Id)

		Chief_Functionary = []
		chiefD = driver.find_element_by_xpath('//*[@id="tps_slideContainer_4541"]/div/div/div/div/div/div[3]/div[3]/div[2]')
		chiefstr = str(chiefD.text)
		Chief_Functionary.append(chiefstr)
		Chief_Functionary = '\n'.join(Chief_Functionary)
		print("Chief Functionary: " + Chief_Functionary)


		Chairman = []
		ChairmanT = driver.find_element_by_xpath('//*[@id="tps_slideContainer_4541"]/div/div/div/div/div/div[3]/div[4]/div[2]')
		charmanstr = str(ChairmanT.text)
		Chairman.append(charmanstr)
		Chairman = '\n'.join(Chairman)
		print("Chairman: " + Chairman)


		Registered_With = []
		RegisteredT = driver.find_element_by_xpath('//*[@id="tps_slideContainer_4541"]/div/div/div/div/div/div[5]/div[1]/div[2]')
		Registeredstr = str(RegisteredT.text)
		Registered_With.append(Registeredstr)
		Registered_With = '\n'.join(Registered_With)
		print("Registered With: " + Registered_With)


		Type_NGO = []
		TypeT = driver.find_element_by_xpath('//*[@id="tps_slideContainer_4541"]/div/div/div/div/div/div[5]/div[2]/div[2]')
		Typestr = str(TypeT.text)
		Type_NGO.append(Typestr)
		Type_NGO = '\n'.join(Type_NGO)
		print("Type of NGO: " + Type_NGO)


		Registration_Number = []
		Registration = driver.find_element_by_xpath('//*[@id="tps_slideContainer_4541"]/div/div/div/div/div/div[5]/div[3]/div[2]')
		Registrationstr = str(Registration.text)
		Registration_Number.append(Registrationstr)
		Registration_Number = '\n'.join(Registration_Number)
		print("Registration Number: " + Registration_Number)

		City_Registration = []
		CityR = driver.find_element_by_xpath('//*[@id="tps_slideContainer_4541"]/div/div/div/div/div/div[5]/div[4]/div[2]')
		Citystr = str(CityR.text)
		City_Registration.append(Citystr)
		City_Registration = '\n'.join(City_Registration)
		print("City of Registration: " + City_Registration)

		State_Registration = []
		State_RegistrationR = driver.find_element_by_xpath('//*[@id="tps_slideContainer_4541"]/div/div/div/div/div/div[5]/div[5]/div[2]')
		State_Registrationstr = str(State_RegistrationR.text)
		State_Registration.append(State_Registrationstr)
		State_Registration = '\n'.join(State_Registration)
		print("State of Registration: " + State_Registration)

		Date_Registration = []
		Date_RegistrationR = driver.find_element_by_xpath('//*[@id="tps_slideContainer_4541"]/div/div/div/div/div/div[5]/div[6]/div[2]')
		Date_Registrationstr = str(Date_RegistrationR.text)
		Date_Registration.append(State_Registrationstr)
		Date_Registration = '\n'.join(Date_Registration)
		print("State of Registration: " + Date_Registration)

		Frca_Registration = []
		Frca_RegistrationR = driver.find_element_by_xpath('//*[@id="tps_slideContainer_4541"]/div/div/div/div/div/div[5]/div[7]/div[2]')
		Frca_Registrationstr = str(Frca_RegistrationR.text)
		Frca_Registration.append(Frca_Registrationstr)
		Frca_Registration = '\n'.join(Frca_Registration)
		print("Frca: " + Frca_Registration)
		

		certificate = []
		certificateR = driver.find_element_by_xpath('//*[@id="tps_slideContainer_4541"]/div/div/div/div/div/div[5]/div[7]/div[2]')
		certificatestr = str(certificateR.text)
		certificate.append(certificatestr)
		certificate = '\n'.join(certificate)
		print("NGO Registration certificate: " + certificate)

		City = []                             
		CityR = driver.find_element_by_xpath('//*[@id="contact details"]/div[1]/div[2]/a/span')
		Citystr = str(CityR.text)
		City.append(Citystr)
		City = '\n'.join(City)
		print("City: " + City)

		State = []
		StateR = driver.find_element_by_xpath('//*[@id="contact details"]/div[2]/div[2]')
		Statestr = str(StateR.text)
		State.append(Statestr)
		State = '\n'.join(State)
		print("State: " + State)

		Country = []
		CountryR = driver.find_element_by_xpath('//*[@id="contact details"]/div[3]/div[2]/span/span')
		Countrystr = str(CountryR.text)
		Country.append(Countrystr)
		Country = '\n'.join(Country)
		print("Country: " + Country)

		Telephone = []
		TelephoneR = driver.find_element_by_xpath('//*[@id="contact details"]/div[4]/div[2]/span')
		Telephonestr = str(TelephoneR.text)
		Telephone.append(Telephonestr)
		Telephone = '\n'.join(Telephone)
		print("Telephone: " + Telephone)
		try:
			Mobile = []                             
			MobileR = driver.find_element_by_xpath('//*[@id="contact details"]/div[5]/div[2]')
			Mobilestr = str(MobileR.text)
			Mobile.append(Mobilestr)
			Mobile = '\n'.join(Mobile)
			if Mobile == "":
				Mobile = "not avalaible"
			print("Mobile: " + Mobile)
		except:
			pass

		Address = []
		AddressR = driver.find_element_by_xpath('//*[@id="contact details"]/div[6]/div[2]/span')
		Addressstr = str(AddressR.text)
		Address.append(Addressstr)
		Address = '\n'.join(Address)
		print("Address: " + Address)

		Email = []
		EmailR = driver.find_element_by_xpath('//*[@id="contact details"]/div[7]/div[2]')
		Emailstr = str(EmailR.text)
		Email.append(Emailstr)
		Email = '\n'.join(Email)
		print("Email: " + Email)

		Website = []
		WebsiteR = driver.find_element_by_xpath('//*[@id="contact details"]/div[8]/div[2]')
		Websitestr = str(WebsiteR.text)
		Website.append(Websitestr)
		Website = '\n'.join(Website)
		print("Website: " + Website)



		fat.append(Ngo_name)
		fat.append(Unique_Id)
		fat.append(Chief_Functionary)
		fat.append(Chairman)
		fat.append(Registered_With)
		fat.append(Type_NGO)
		fat.append(Registration_Number)
		fat.append(City_Registration)
		fat.append(State_Registration)
		fat.append(Date_Registration)
		fat.append(Frca_Registration)
		fat.append(certificate)
		fat.append(City)
		fat.append(State)
		fat.append(Country)
		fat.append(Telephone)
		fat.append(Mobile)
		fat.append(Address)
		fat.append(Email)
		fat.append(Website)


		appendRow(fat)



def start():
	header= ['Ngo_Name', 'Unique Id of VO/NGO', 'Chief Functionary ', 'Chairman', 'Registered With', 'Type of NGO', 'Registration Number', 'City of Registration', 'State of Registration','Date of Registration', 'Frca', 'NGO Registration certificate', 'City', 'State', 'Country', 'Telephone', 'Mobile Number', 'Address', 'Email', 'Website']
	print ("adding the heading in the google sheet1....")
	appendRow(header)



start()

scrape_ngo_list(START_URL)

if __name__ == "__main__":
	with open ("ngo_links.csv") as url_obj:
		csv_url_reader(url_obj)



