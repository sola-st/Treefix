# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_quoting.py
parser = all_parsers
expected = DataFrame([[1, 2, "cat"]], columns=["a", "b", "c"])

data = 'a,b,c\n1,2,"cat"'
new_data = data.replace('"', quote_char)

result = parser.read_csv(StringIO(new_data), quotechar=quote_char)
tm.assert_frame_equal(result, expected)
