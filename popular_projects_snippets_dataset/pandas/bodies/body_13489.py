# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
frame = tm.makeTimeDataFrame()
create_sql = sql.get_schema(frame, "test")
lines = create_sql.splitlines()
for line in lines:
    tokens = line.split(" ")
    if len(tokens) == 2 and tokens[0] == "A":
        assert tokens[1] == "DATETIME"

create_sql = sql.get_schema(frame, "test", keys=["A", "B"])
lines = create_sql.splitlines()
assert 'PRIMARY KEY ("A", "B")' in create_sql
cur = sqlite_buildin.cursor()
cur.execute(create_sql)
