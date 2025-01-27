# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
frame = DataFrame({"Col1": [1.1, 1.2], "Col2": [2.1, 2.2]})
create_sql = sql.get_schema(frame, "test", con=self.conn, keys="Col1")
constraint_sentence = 'CONSTRAINT test_pk PRIMARY KEY ("Col1")'
assert constraint_sentence in create_sql

# multiple columns as key (GH10385)
create_sql = sql.get_schema(test_frame1, "test", con=self.conn, keys=["A", "B"])
constraint_sentence = 'CONSTRAINT test_pk PRIMARY KEY ("A", "B")'
assert constraint_sentence in create_sql
