# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
df = DataFrame({"col": [1, 2]})
expected = """\
"","col"
"0","1"
"1","2"
"""

with tm.ensure_clean("test.csv") as path:
    df.to_csv(path, quoting=1)  # 1=QUOTE_ALL
    with open(path) as f:
        assert f.read() == expected

expected = """\
$$,$col$
$0$,$1$
$1$,$2$
"""

with tm.ensure_clean("test.csv") as path:
    df.to_csv(path, quoting=1, quotechar="$")
    with open(path) as f:
        assert f.read() == expected

with tm.ensure_clean("test.csv") as path:
    with pytest.raises(TypeError, match="quotechar"):
        df.to_csv(path, quoting=1, quotechar=None)
