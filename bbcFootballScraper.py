import requests, bs4
print 'hello world'
footballResults = requests.get('http://www.bbc.com/sport/football/results')
print footballResults
#parse the html with beautiful soup
soupPage = bs4.BeautifulSoup(footballResults.text)
##get all of the match details
matchDetails = soupPage.select('td.match-details')
#scores = soupPage.select('span.score')
scores = soupPage.find_all(title = 'Score')
for s in scores:
	print s.getText()
