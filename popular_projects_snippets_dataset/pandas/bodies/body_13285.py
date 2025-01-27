# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
cur = conn.cursor()
stmt = """CREATE TABLE iris (
            "SepalLength" REAL,
            "SepalWidth" REAL,
            "PetalLength" REAL,
            "PetalWidth" REAL,
            "Name" TEXT
        )"""
cur.execute(stmt)
with iris_file.open(newline=None) as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    stmt = "INSERT INTO iris VALUES(?, ?, ?, ?, ?)"
    cur.executemany(stmt, reader)
