# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
# GH 21041
bio = io.BytesIO()
df = tm.makeDataFrame()
df.index.name = "index"
with tm.ensure_clean() as path:
    df.to_stata(bio, version=version)
    bio.seek(0)
    with open(path, "wb") as dta:
        dta.write(bio.read())
    reread = read_stata(path, index_col="index")
tm.assert_frame_equal(df, reread)
