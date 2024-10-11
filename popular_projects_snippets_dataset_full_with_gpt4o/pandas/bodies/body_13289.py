# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
cur = conn.cursor()
stmt = """CREATE TABLE types (
                    "TextCol" TEXT,
                    "DateCol" TEXT,
                    "IntDateCol" INTEGER,
                    "IntDateOnlyCol" INTEGER,
                    "FloatCol" REAL,
                    "IntCol" INTEGER,
                    "BoolCol" INTEGER,
                    "IntColWithNull" INTEGER,
                    "BoolColWithNull" INTEGER
                )"""
cur.execute(stmt)

stmt = """
            INSERT INTO types
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
cur.executemany(stmt, types_data)
