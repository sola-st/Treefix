# Extracted from ./data/repos/pandas/pandas/tests/config/test_config.py
cf.register_option("a", 1, "doc")
cf.register_option("b.c", "hullo", "doc2")
cf.register_option("b.b", None, "doc2")

# gets of existing keys succeed
assert cf.get_option("a") == 1
assert cf.get_option("b.c") == "hullo"
assert cf.get_option("b.b") is None

# gets of non-existent keys fail
msg = r"No such keys\(s\): 'no_such_option'"
with pytest.raises(OptionError, match=msg):
    cf.get_option("no_such_option")
