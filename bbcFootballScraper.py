import requests, bs4
print 'hello world'
footballResults = requests.get('http://www.bbc.com/sport/football/results')
print footballResults
#parse the html with beautiful soup
soupPage = bs4.BeautifulSoup(footballResults.text)
##get all of the match details
sectionDetails = soupPage.select('table.table-stats')
#get each league table
for section in sectionDetails:
	print "========"	
	matchDetails = section.select('td.match-details')
	#get the date of the match
	if len(section)>0 and len(matchDetails)>0:
		print ' '.join(section.caption.string.encode('utf-8').split()[-4:])
	scores = soupPage.select('span.score')
	#get each match result
	for md in matchDetails:
        	print md.select('span.team-home')[0].getText().strip()
        	#print md
        	if md.find(title = 'Score') != None:
                	print md.find(title = 'Score').getText().strip()
		else:
                	print md.find(title = 'Postponed').getText().strip()
        	print md.select('span.team-away')[0].getText().strip()
	        print '--------'


