import requests, bs4
print 'hello world'
footballResults = requests.get('http://www.bbc.com/sport/football/results')
print footballResults
#parse the html with beautiful soup
soupPage = bs4.BeautifulSoup(footballResults.text)
##get all of the match details
sectionDetails = soupPage.select('table.table-stats')
for section in sectionDetails:
	print "========"	
	matchDetails = section.select('td.match-details')
	if len(section)>0 and len(matchDetails)>0:
		print ' '.join(section.caption.string.encode('utf-8').split()[-4:])
#	print section.previous_elements
#	if "table-header" in section.previousSibling:
#		print 'new date! ' + section.previousSibling.getText()
	scores = soupPage.select('span.score')
	for md in matchDetails:
        	print md.select('span.team-home')[0].getText().strip()
        	#print md
        	if md.find(title = 'Score') != None:
                	print md.find(title = 'Score').getText().strip()
		else:
                	print md.find(title = 'Postponed').getText().strip()
        	print md.select('span.team-away')[0].getText().strip()
	        print '--------'

#matchDetails = soupPage.select('td.match-details')
#scores = soupPage.select('span.score')
#for md in matchDetails:
 #       print md.select('span.team-home')[0].getText().strip()
  #      #print md
   #     if md.find(title = 'Score') != None:
    #            print md.find(title = 'Score').getText().strip()
     #   else:
      #          print md.find(title = 'Postponed').getText().strip()
       # print md.select('span.team-away')[0].getText().strip()
       # print '--------'
#scores = soupPage.find_all(title = 'Score')

#for s in scores:
#  print s.getText()
