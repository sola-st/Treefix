# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
# GH 22610
data = ["\ud800foo"]
ser = pd.Series(data, index=pd.Index(data))
with tm.ensure_clean("test.csv") as path:
    ser.to_csv(path, errors=errors)
