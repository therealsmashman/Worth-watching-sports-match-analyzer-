import MySQLdb as mdb
import sys, requests, bs4, codecs, urllib2

def insertMatchData(pageUrl, sectionSeperator, dateTitle ,leageTitle, leaguePos,
			 matchSeperator, scoreSeperator, homeSeperator, awaySeperator):
	try:
		con = mdb.connect('localhost', 'testuser', 'testSimon', 'testdb');

		cur = con.cursor()
		cur.execute("DROP TABLE IF EXISTS rugbyGames")
		cur.execute('''CREATE TABLE rugbyGames(Id INT PRIMARY KEY AUTO_INCREMENT, 
				MatchDate VARCHAR(100) NOT NULL, 				
				League VARCHAR(100) NOT NULL, 
				HomeTeam VARCHAR(100), 
				HomeScore INT NOT NULL, 
				AwayTeam VARCHAR(100) NOT NULL, 
				AwayScore INT NOT NULL
				)''')##Postponed BOOLEAN
		#cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
		#cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
		#cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
		#cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
		#cur.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")
        	#footballResults = requests.get('http://www.bbc.com/sport/football/results')
		pageToScrape = open(pageUrl).read()
		#parse the html with beautiful soup
		#soupPage = bs4.BeautifulSoup(footballResults.text)
		soupPage = bs4.BeautifulSoup(pageToScrape)
		##get all of the match details
		sectionDetails = soupPage.select(sectionSeperator)
		#get each league table
		for section in sectionDetails:
		        print "========"
			if len(section.select(dateTitle))>0:
				date = section.select(dateTitle)[0].getText().strip()
				print date
			if len(section.select(leageTitle))>leaguePos:				 
				league = section.select(leageTitle)[leaguePos].getText().strip()     
				print league  
		        matchDetails = section.select(matchSeperator)
		        for md in matchDetails:
		                print '----------------'
				score = md.select(scoreSeperator)[0].getText().encode('utf-8').strip().split('-')
		                home = md.select(homeSeperator)[0].getText().strip()
		                #home += " : " +score[0]
		                print home + " : " + score[0]
		                away = md.select(awaySeperator)[0].getText().strip() #+ " : "
		                #away += score[1]
		                print away +" : " + score[1]
				cur.execute('''INSERT INTO 
					rugbyGames(MatchDate,League,HomeTeam,HomeScore,AwayTeam,AwayScore) 
					VALUES("'''+date+'","'+league+'","'+home+'","'+score[0]+'","'+away+'","'+score[1] +'")')
		con.commit()
	except mdb.Error, e:
	    if con:
		 con.rollback()
	    print "Error %d: %s" % (e.args[0],e.args[1])
	    sys.exit(1)

	finally:

	    if con:
		con.close()

def rugby():
        insertMatchData("examplePages/sportRugby.html",
                       'div.data-table',
			'h2.table-header',
			'p.table-description',
                       0,
                       'tr.result',
                       'td.vs',
                       'td.home-team',
                       'td.away-team')

rugby()

