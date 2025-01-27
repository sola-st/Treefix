# Extracted from ./data/repos/pandas/pandas/tests/io/test_orc.py
# GH44554
# PyArrow gained ORC write support with the current argument order
msg = "The dtype of one or more columns is not supported yet."
with pytest.raises(NotImplementedError, match=msg):
    df_not_supported.to_orc()
