# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
# see gh-21696
# see gh-20353
df = DataFrame({"a": ["x", "y", "z"]})
expected_rows = ["x", "y", "z"]
expected = "manual header\n" + tm.convert_rows_list_to_csv_str(expected_rows)
with tm.ensure_clean("test.txt") as path:
    with open(path, "w", newline="") as f:
        f.write("manual header\n")
        df.to_csv(f, header=None, index=None)

    with open(path, "rb") as f:
        assert f.read() == bytes(expected, "utf-8")
