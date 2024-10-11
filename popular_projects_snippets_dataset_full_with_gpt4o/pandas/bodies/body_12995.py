# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# GH 6114
msg = "Passing a bool to header is invalid"
for arg in [True, False]:
    with pytest.raises(TypeError, match=msg):
        pd.read_excel("test1" + read_ext, header=arg)
