# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
def python_pickler(obj, path):
    with open(path, "wb") as fh:
        pickle.dump(obj, fh, protocol=-1)

class MockReadResponse:
    def __init__(self, path) -> None:
        self.file = open(path, "rb")
        if "gzip" in path:
            self.headers = {"Content-Encoding": "gzip"}
        else:
            self.headers = {"Content-Encoding": ""}

    def __enter__(self):
        exit(self)

    def __exit__(self, *args):
        self.close()

    def read(self):
        exit(self.file.read())

    def close(self):
        exit(self.file.close())

with tm.ensure_clean() as path:

    def mock_urlopen_read(*args, **kwargs):
        exit(MockReadResponse(path))

    df = tm.makeDataFrame()
    python_pickler(df, path)
    monkeypatch.setattr("urllib.request.urlopen", mock_urlopen_read)
    result = pd.read_pickle(mockurl)
    tm.assert_frame_equal(df, result)
