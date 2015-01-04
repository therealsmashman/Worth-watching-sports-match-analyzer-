import requests, bs4
print 'hello world'
footballResults = requests.get('http://www.bbc.com/sport/football/results')
print footballResults
#parse the html with beautiful soup
soupPage = bs4.BeautifulSoup(footballResults.text)
##get all of the match details

matchDetails = soupPage.select('td.match-details')
#scores = soupPage.select('span.score')
for md in matchDetails:
	print md.select('span.team-home')[0].getText().strip()
	#print md
	print md.find(title = 'Score').getText().strip()
	print md.select('span.team-away')[0].getText().strip()
	print '--------'
#scores = soupPage.find_all(title = 'Score')

#for s in scores:
#	print s.getText()
