# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# GH 41893
with pytest.raises(ValueError, match="No axis named bad for object type DataFrame"):
    mi_styler.applymap_index(lambda v: "attr: val;", axis="bad")._compute()
