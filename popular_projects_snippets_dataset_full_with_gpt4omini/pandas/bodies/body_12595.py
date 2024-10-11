# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
with tm.ensure_clean("test.json") as path:
    for df in [float_frame, int_frame, datetime_frame]:
        df.to_json(path)
        read_json(path)
