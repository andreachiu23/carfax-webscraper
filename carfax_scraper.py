from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client

my_url = 'https://www.carfax.com/Used-Cars-in-Old-Bridge-NJ_c22311'

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grab all listings
listings = page_soup.findAll("article", {"class":"srp-list-item"})

# open and label csv to write to
out_file = "carfax_data.csv"
header = "Description,Loc/Dist,Price,Mileage,Link"
f = open(out_file, "w")
f.write(header + "\n")

# loop through each listing and grab attributes
for listing in listings:

	# make / model description
	name_container = listing.findAll("span", {"class":"srp-list-item-basic-info-model"})
	name = name_container[0].text

	# loc and distance  
	loc_container = listing.findAll("div", {"class": "srp-list-item-dealership-location"})
	loc = loc_container[0].text

	# price
	price_container = listing.findAll("span", {"class": "srp-list-item-price"})
	price = price_container[0].text

	# mileage
	mile_container = listing.findAll("span", {"class": "srp-list-item-basic-info-value"})
	mileage = mile_container[0].text

	# link to page
	link = listing.a["href"]

	f.write(name + ", " + loc.replace(",","") + ", " + price.replace(",","") + ", " + mileage.replace(",","") + ", " + "https://www.carfax.com" + link.replace("'","") + "\n")


f.close()