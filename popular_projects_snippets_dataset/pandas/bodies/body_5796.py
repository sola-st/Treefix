# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
# GH 48833
with pytest.raises(
    NotImplementedError, match=".* not implemented for <class 'object'>"
):
    comparison_op(data, object())
