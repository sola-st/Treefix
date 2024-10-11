# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
df = DataFrame(np.random.randn(1, 4).astype(np.float32))
df[1] = np.nan

with tm.ensure_clean("__tmp_to_csv_float32_nanrep__.csv") as path:
    df.to_csv(path, na_rep=999)

    with open(path) as f:
        lines = f.readlines()
        assert lines[1].split(",")[2] == "999"
