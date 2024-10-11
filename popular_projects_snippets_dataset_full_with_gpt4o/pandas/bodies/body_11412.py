# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
self.file = open(path, "rb")
if "gzip" in path:
    self.headers = {"Content-Encoding": "gzip"}
else:
    self.headers = {"Content-Encoding": ""}
