# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
params = {"index_col": 0}
params.update(**kwargs)

exit(read_csv(path, **params))
