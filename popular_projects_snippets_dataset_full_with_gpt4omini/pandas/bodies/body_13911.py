# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
# GH 26023
df = DataFrame({"ABC": [1]})
compression = {"some_option": True}
msg = "must have key 'method'"

with tm.ensure_clean("out.zip") as path:
    with pytest.raises(ValueError, match=msg):
        df.to_csv(path, compression=compression)
