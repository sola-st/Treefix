# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
"""
        Binary file objects should honor a specified encoding.

        GH 23854 and GH 13068 with binary handles
        """
# example from GH 23854
content = "a, b, 🐟".encode("utf-8-sig")
buffer = io.BytesIO(content)
df = pd.read_csv(buffer, encoding="utf-8-sig")

buffer = io.BytesIO()
df.to_csv(buffer, mode=mode, encoding="utf-8-sig", index=False)
buffer.seek(0)  # tests whether file handle wasn't closed
assert buffer.getvalue().startswith(content)

# example from GH 13068
with tm.ensure_clean() as path:
    with open(path, "w+b") as handle:
        DataFrame().to_csv(handle, mode=mode, encoding="utf-8-sig")

        handle.seek(0)
        assert handle.read().startswith(b'\xef\xbb\xbf""')
