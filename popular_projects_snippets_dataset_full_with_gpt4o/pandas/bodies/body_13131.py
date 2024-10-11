# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_xlrd.py
# GH 29375
from xlrd.biffh import XLRDError

path = datapath("io", "data", "excel", "test1.xlsx")
with pytest.raises(XLRDError, match="Excel xlsx file; not supported"):
    pd.read_excel(path, engine="xlrd")
