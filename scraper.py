#!/usr/bin/env python3

###
#The following script is a python scraper designed for searching webpages for the amount 
# of times that a certain word appears on that page. 
# One potential use of such a program would be academic research.
# For example: economic policy uncertainty indices which are based upon the amount of times certain
# terms appear in news papers could employ this script to search webpages for those terms.
###

import requests, csv

fileName = "results"

#checks to see if term has already been searched
def updateTerm(term, count, f):
	for row in f:
		if row['Term'] == term:
			row['Count'] = str(count)
			return (1)
	return (0)	
		
#addRes adds the result of search to the results file, creates new file if it does not exist
def addRes(term, count, url):
	try:
		boyo = open(fileName)
		boyo.close()
	except FileNotFoundError:
		with open(fileName, 'w') as csvfile:
			filewriter = csv.writer(csvfile, delimiter=':', quotechar='|', quoting=csv.QUOTE_MINIMAL)
			filewriter.writerow(["webpage url: ", url])
			filewriter.writerow(['TERM', 'COUNT'])
	with open(fileName, 'a') as f:
		writer = csv.writer(f)
		writer.writerow([term, count])

#Search searches through page.txt to find the word in question, which is given by the user.
def search(url):
	count = 0
	term = input("\nPlease insert the term you wish to search for: ")
	print ("searching for " + term + "...")
	check = open("page.txt")
	#may need to change this to see if it only checks line once
	for line in check:
		if term in line:
			count = count + 1
	print ("The term " + term + " was found", count, "times.\n This result has been saved to the file", fileName, ".")
	addRes(term, count, url)

########################################################
#Script srarts excuting from here
########################################################

#The script prompts the user to state if they wish to download a webpage for scraping
print ("This is a python scraper for ascertaining how many times a given word appears on a webapage.")
command = input("Please enter webpage url to be downloaded and scraped: ")
print ("Dowloading webpage....")
print ("webpage saved as page.txt")
res = requests.get(command)
res.raise_for_status()
fileName = input("You will now need to insert the name of the file you wish your results to be saved too. \n If you wish to add to an exisiting file simply enter its name now.\n BE SURE TO USE A NEW FILE WHEN SCRAPING A NEW URL.\n The '.csv' extension will be added for you.\n\n Please insert the name of the file you wish your results to be saved too: ")
fileName = fileName + ".csv"
downloadedFile = open("page.txt", 'wb')
for chunk in res.iter_content(100000):
	downloadedFile.write(chunk)
downloadedFile.close()

#Carries out scraping the first term and then prompts the user for more input.
temp = '1'
while (temp == '1'):
	search(command)
	n = input ("\nPlease enter '1' if you would like to search for another term. Enter 2 to exit: ")
	temp = n
print ("Exiting... Please be sure to deleted page.txt if you wish to scrape another webpage")