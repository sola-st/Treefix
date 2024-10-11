# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
"""
        Change directory and set engine for ExcelFile objects.
        """
func = partial(pd.ExcelFile, engine=engine)
monkeypatch.chdir(datapath("io", "data", "excel"))
monkeypatch.setattr(pd, "ExcelFile", func)
