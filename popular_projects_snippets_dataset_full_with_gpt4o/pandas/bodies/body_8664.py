# Extracted from ./data/repos/pandas/pandas/tests/config/test_config.py
msg = "Must provide an even number of non-keyword arguments"
with pytest.raises(ValueError, match=msg):
    cf.set_option("a.b", 2, "b.c")
