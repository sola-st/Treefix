# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
columns = ["index", "A", "B"]
data = [
    ("2000-01-03 00:00:00", 2**31 - 1, -1.987670),
    ("2000-01-04 00:00:00", -29, -0.0412318367011),
    ("2000-01-05 00:00:00", 20000, 0.731167677815),
    ("2000-01-06 00:00:00", -290867, 1.56762092543),
]
exit(DataFrame(data, columns=columns))
