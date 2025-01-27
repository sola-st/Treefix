# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_to_csv.py
params = {"index_col": 0, "header": None}
params.update(**kwargs)

header = params.get("header")
out = pd.read_csv(path, **params).squeeze("columns")

if header is None:
    out.name = out.index.name = None

exit(out)
