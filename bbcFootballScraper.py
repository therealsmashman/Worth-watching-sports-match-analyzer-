import requests, bs4, codecs
import urllib2

def printMatchData(pageUrl, sectionSeperator, matchSeperator, scoreSeperator, homeSeperator, awaySeperator):
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
                matchDetails = section.select(matchSeperator)
                for md in matchDetails:
                        score = md.select(scoreSeperator)[0].getText().encode('utf-8').strip().split('-')
                        home = md.select(homeSeperator)[0].getText().strip()
                        home += " : " +score[0]
                        print home
                        away = md.select(awaySeperator)[0].getText().strip() + " : "
                        away += score[1]
                        print away
                        print '--------'
        



def rugby():
        printMatchData("examplePages/sportRugby.html",
                       'div.data-table',
                       'tr.result',
                       'td.vs',
                       'td.home-team',
                       'td.away-team')
'''
        #footballResults = requests.get('http://www.bbc.com/sport/football/results')
        footballResults = open("examplePages/sportRugby.html").read()
        #print footballResults
        #parse the html with beautiful soup
        #soupPage = bs4.BeautifulSoup(footballResults.text)
        soupPage = bs4.BeautifulSoup(footballResults)
        ##get all of the match details
        sectionDetails = soupPage.select('div.data-table')
        #get each league table
        for section in sectionDetails:
                print "========"        
                matchDetails = section.select('tr.result')
                for md in matchDetails:
                        score = md.select('td.vs')[0].getText().encode('utf-8').strip().split('-')
                        home = md.select('td.home-team')[0].getText().strip()
                        home += " : " +score[0]
                        print home
                        away = md.select('td.away-team')[0].getText().strip() + " "
                        away += score[1]
                        print away
                        print '--------'
                matchDetails = section.select('tr.alternate')
                for md in matchDetails:
                        score = md.select('td.vs')[0].getText().encode('utf-8').strip().split('-')
                        home = md.select('td.home-team')[0].getText().strip() + " : " 
                        home += score[0]
                        print home
                        print md.select('td.vs')[0].getText().strip()                        
                        away = md.select('td.away-team')[0].getText().strip() + " "
                        away += score[1]
                        print away
                        print '--------'
'''
                
def footBall():
        printMatchData("examplePages/sportFootball.html",
                       'table.table-stats',
                       'td.match-details',
                       'span.score',
                       'span.team-home',
                       'span.team-away')

'''         
        #footballResults = requests.get('http://www.bbc.com/sport/football/results')
        footballResults = open("examplePages/sportFootball.html").read()
        #print footballResults
        #parse the html with beautiful soup
        #soupPage = bs4.BeautifulSoup(footballResults.text)
        soupPage = bs4.BeautifulSoup(footballResults)
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
                        #if md.find(title = 'Score') != None:
                        #if len(md.select("span.score"))>0:
                        print md.select("span.score")[0].getText().strip()
                        #else:
                        #        print md.find(title = 'Postponed').getText().strip()
                        print md.select('span.team-away')[0].getText().strip()
                        print '--------'

'''        
  

print 'hello world'
footBall()
