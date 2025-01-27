# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_non_unique.py
# classes has unique keys
classes = DataFrame([["1", "2"], ["3", "4"]], columns=["c", "d"], index=["a", "b"])
styler.set_td_classes(classes=classes)  # OK

# classes has non-unique columns
classes = DataFrame([["1", "2"], ["3", "4"]], columns=["c", "c"], index=["a", "b"])
with pytest.raises(KeyError, match="Classes render only if `classes` has unique"):
    styler.set_td_classes(classes=classes)

# classes has non-unique index
classes = DataFrame([["1", "2"], ["3", "4"]], columns=["c", "d"], index=["a", "a"])
with pytest.raises(KeyError, match="Classes render only if `classes` has unique"):
    styler.set_td_classes(classes=classes)
