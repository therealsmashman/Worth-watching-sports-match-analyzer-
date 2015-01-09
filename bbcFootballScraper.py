import requests, bs4, codecs
import urllib2

def rugby():
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
                
def footBall():
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
                        if md.find(title = 'Score') != None:
                                print md.find(title = 'Score').getText().strip()
                        else:
                                print md.find(title = 'Postponed').getText().strip()
                        print md.select('span.team-away')[0].getText().strip()
                        print '--------'


print 'hello world'
rugby()
