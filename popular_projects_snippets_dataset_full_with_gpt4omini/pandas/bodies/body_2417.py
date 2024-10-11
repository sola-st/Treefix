# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
f = float_frame
ix = f.loc

# individual value
for col in f.columns:
    ts = f[col]
    for idx in f.index[::5]:
        assert ix[idx, col] == ts[idx]
