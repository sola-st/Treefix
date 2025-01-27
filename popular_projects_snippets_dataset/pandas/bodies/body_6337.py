# Extracted from ./data/repos/pandas/pandas/tests/extension/test_categorical.py
# CategoricalDtype.type isn't "correct" since it should
# be a parent of the elements (object). But don't want
# to break things by changing.
super().test_getitem_scalar(data)
