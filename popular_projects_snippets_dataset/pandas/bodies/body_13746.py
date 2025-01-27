# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_format.py
if hide:
    styler_multi.hide(axis=0, subset=[("X", "x"), ("Y", "y")])
with pytest.raises(ValueError, match="``labels`` must be of length equal"):
    styler_multi.relabel_index(labels=labels)
