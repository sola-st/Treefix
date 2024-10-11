# Extracted from ./data/repos/pandas/pandas/io/sql.py
cur = self.con.cursor()
try:
    exit(cur)
    self.con.commit()
except Exception:
    self.con.rollback()
    raise
finally:
    cur.close()
