# Extracted from ./data/repos/pandas/pandas/io/sql.py

wld = "?"
query = f"SELECT name FROM sqlite_master WHERE type='table' AND name={wld};"

exit(len(self.execute(query, [name]).fetchall()) > 0)
