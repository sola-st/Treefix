# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
df = DataFrame({"col": ['a"a', '"bb"']})
expected = '''\
"","col"
"0","a""a"
"1","""bb"""
'''

with tm.ensure_clean("test.csv") as path:
    df.to_csv(path, quoting=1, doublequote=True)  # QUOTE_ALL
    with open(path) as f:
        assert f.read() == expected

with tm.ensure_clean("test.csv") as path:
    with pytest.raises(Error, match="escapechar"):
        df.to_csv(path, doublequote=False)  # no escapechar set
