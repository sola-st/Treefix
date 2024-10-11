# Extracted from https://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python
# server_version.py - retrieve and display database server version

import MySQLdb

conn = MySQLdb.connect (host = "localhost",
                        user = "testuser",
                        passwd = "testpass",
                        db = "test")
cursor = conn.cursor ()
cursor.execute ("SELECT VERSION()")
row = cursor.fetchone ()
print "server version:", row[0]
cursor.close ()
conn.close ()

