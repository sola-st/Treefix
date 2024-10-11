# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
# empty frame (GH#2778)
df = DataFrame(columns=["x"])
for m in ["pad", "backfill"]:
    df.x.fillna(method=m, inplace=True)
    df.x.fillna(method=m)
