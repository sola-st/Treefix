# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
df = DataFrame(
    {
        "c_bool": [True, False],
        "c_float": [1.0, 3.2],
        "c_int": [42, np.nan],
        "c_string": ["a", "b,c"],
    }
)

expected_rows = [
    ",c_bool,c_float,c_int,c_string",
    "0,True,1.0,42.0,a",
    '1,False,3.2,,"b,c"',
]
expected = tm.convert_rows_list_to_csv_str(expected_rows)

result = df.to_csv()
assert result == expected

result = df.to_csv(quoting=None)
assert result == expected

expected_rows = [
    ",c_bool,c_float,c_int,c_string",
    "0,True,1.0,42.0,a",
    '1,False,3.2,,"b,c"',
]
expected = tm.convert_rows_list_to_csv_str(expected_rows)

result = df.to_csv(quoting=csv.QUOTE_MINIMAL)
assert result == expected

expected_rows = [
    '"","c_bool","c_float","c_int","c_string"',
    '"0","True","1.0","42.0","a"',
    '"1","False","3.2","","b,c"',
]
expected = tm.convert_rows_list_to_csv_str(expected_rows)

result = df.to_csv(quoting=csv.QUOTE_ALL)
assert result == expected

# see gh-12922, gh-13259: make sure changes to
# the formatters do not break this behaviour
expected_rows = [
    '"","c_bool","c_float","c_int","c_string"',
    '0,True,1.0,42.0,"a"',
    '1,False,3.2,"","b,c"',
]
expected = tm.convert_rows_list_to_csv_str(expected_rows)
result = df.to_csv(quoting=csv.QUOTE_NONNUMERIC)
assert result == expected

msg = "need to escape, but no escapechar set"
with pytest.raises(csv.Error, match=msg):
    df.to_csv(quoting=csv.QUOTE_NONE)

with pytest.raises(csv.Error, match=msg):
    df.to_csv(quoting=csv.QUOTE_NONE, escapechar=None)

expected_rows = [
    ",c_bool,c_float,c_int,c_string",
    "0,True,1.0,42.0,a",
    "1,False,3.2,,b!,c",
]
expected = tm.convert_rows_list_to_csv_str(expected_rows)
result = df.to_csv(quoting=csv.QUOTE_NONE, escapechar="!")
assert result == expected

expected_rows = [
    ",c_bool,c_ffloat,c_int,c_string",
    "0,True,1.0,42.0,a",
    "1,False,3.2,,bf,c",
]
expected = tm.convert_rows_list_to_csv_str(expected_rows)
result = df.to_csv(quoting=csv.QUOTE_NONE, escapechar="f")
assert result == expected

# see gh-3503: quoting Windows line terminators
# presents with encoding?
text_rows = ["a,b,c", '1,"test \r\n",3']
text = tm.convert_rows_list_to_csv_str(text_rows)
df = read_csv(StringIO(text))

buf = StringIO()
df.to_csv(buf, encoding="utf-8", index=False)
assert buf.getvalue() == text

# xref gh-7791: make sure the quoting parameter is passed through
# with multi-indexes
df = DataFrame({"a": [1, 2], "b": [3, 4], "c": [5, 6]})
df = df.set_index(["a", "b"])

expected_rows = ['"a","b","c"', '"1","3","5"', '"2","4","6"']
expected = tm.convert_rows_list_to_csv_str(expected_rows)
assert df.to_csv(quoting=csv.QUOTE_ALL) == expected
