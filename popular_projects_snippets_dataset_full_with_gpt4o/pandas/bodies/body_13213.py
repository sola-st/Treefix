# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_sas.py
# see gh-14947
b = StringIO("")

msg = (
    "If this is a buffer object rather than a string "
    "name, you must specify a format string"
)
with pytest.raises(ValueError, match=msg):
    read_sas(b)
