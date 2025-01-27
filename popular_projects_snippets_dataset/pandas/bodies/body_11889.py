# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_read_fwf.py
"""
    read_fwf supports opening files in binary mode.

    GH 18035.
    """
data = """aas aas aas
bba bab b a"""
df_reference = DataFrame(
    [["bba", "bab", "b a"]], columns=["aas", "aas.1", "aas.2"], index=[0]
)
with tm.ensure_clean() as path:
    Path(path).write_text(data)
    with open(path, "rb") as file:
        df = read_fwf(file)
        file.seek(0)
        tm.assert_frame_equal(df, df_reference)
