# Extracted from ./data/repos/pandas/pandas/tests/config/test_config.py
v = cf.is_one_of_factory([None, 12])

v(12)
v(None)
msg = r"Value must be one of None\|12"
with pytest.raises(ValueError, match=msg):
    v(1.1)
