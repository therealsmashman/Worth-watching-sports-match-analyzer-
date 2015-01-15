import MySQLdb as mdb

import sys

try:
    con = mdb.connect('localhost', 'testuser', 'testSimon', 'testdb');

    cur = con.cursor()
    cur.execute("SELECT * FROM rugbyGames")

    rows = cur.fetchall()
    print len(rows)
    for row in rows:
        print row


except mdb.Error, e:

    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)

finally:

    if con:
        con.close()
