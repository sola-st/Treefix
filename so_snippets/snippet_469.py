# Extracted from https://stackoverflow.com/questions/4201455/sqlalchemy-whats-the-difference-between-flush-and-commit
UPDATE accounts SET value = value - 100 WHERE acct = 'A'
UPDATE accounts SET value = value + 100 WHERE acct = 'B'

BEGIN
UPDATE accounts SET value = value - 100 WHERE acct = 'A'
UPDATE accounts SET value = value + 100 WHERE acct = 'B'
COMMIT

                                      # BEGIN issued here
acctA = session.query(Account).get(1) # SELECT issued here
acctB = session.query(Account).get(2) # SELECT issued here

acctA.value -= 100
acctB.value += 100

session.commit()                      # UPDATEs and COMMIT issued here 

                                      # BEGIN issued here
acctA = session.query(Account).get(1) # SELECT issued here
acctB = session.query(Account).get(2) # SELECT issued here

acctA.value -= 100
acctB.value += 100

session.flush()                       # UPDATEs issued here 
session.commit()                      # COMMIT issued here 

