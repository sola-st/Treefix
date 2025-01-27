# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_odf.py
func = functools.partial(pd.read_excel, engine="odf")
monkeypatch.setattr(pd, "read_excel", func)
monkeypatch.chdir(datapath("io", "data", "excel"))
