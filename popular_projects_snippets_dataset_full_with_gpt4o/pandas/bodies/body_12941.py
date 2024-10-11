# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
"""
        Change directory and set engine for read_excel calls.
        """
func = partial(pd.read_excel, engine=engine)
monkeypatch.chdir(datapath("io", "data", "excel"))
monkeypatch.setattr(pd, "read_excel", func)
