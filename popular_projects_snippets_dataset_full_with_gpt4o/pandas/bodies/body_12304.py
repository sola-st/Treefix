# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
# GH 19417
#
# Test that value_labels() returns an empty dict if the file format
# predates supporting value labels.
dpath = datapath("io", "data", "stata", "S4_EDUC1.dta")
with StataReader(dpath) as reader:
    assert reader.value_labels() == {}
