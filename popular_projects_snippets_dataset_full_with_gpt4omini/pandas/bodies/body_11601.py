# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_dialect.py
dialect_name = "mydialect"
parser = all_parsers
data = """\
fruit:vegetable
apple:broccoli
pear:tomato
"""
exp = DataFrame({"fruit": ["apple", "pear"], "vegetable": ["broccoli", "tomato"]})

with tm.with_csv_dialect(dialect_name, delimiter=":"):
    df = parser.read_csv(StringIO(data), dialect=dialect_name)
    tm.assert_frame_equal(df, exp)
