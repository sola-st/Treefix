# Extracted from ./data/repos/pandas/pandas/tests/config/test_config.py
cf.register_option("a", 1, "doc")
cf.register_option("b", 1, "doc2")
cf.deprecate_option("b")

cf.register_option("c.d.e1", 1, "doc3")
cf.register_option("c.d.e2", 1, "doc4")
cf.register_option("f", 1)
cf.register_option("g.h", 1)
cf.register_option("k", 2)
cf.deprecate_option("g.h", rkey="k")
cf.register_option("l", "foo")

# non-existent keys raise KeyError
msg = r"No such keys\(s\)"
with pytest.raises(OptionError, match=msg):
    cf.describe_option("no.such.key")

# we can get the description for any key we registered
assert "doc" in cf.describe_option("a", _print_desc=False)
assert "doc2" in cf.describe_option("b", _print_desc=False)
assert "precated" in cf.describe_option("b", _print_desc=False)
assert "doc3" in cf.describe_option("c.d.e1", _print_desc=False)
assert "doc4" in cf.describe_option("c.d.e2", _print_desc=False)

# if no doc is specified we get a default message
# saying "description not available"
assert "available" in cf.describe_option("f", _print_desc=False)
assert "available" in cf.describe_option("g.h", _print_desc=False)
assert "precated" in cf.describe_option("g.h", _print_desc=False)
assert "k" in cf.describe_option("g.h", _print_desc=False)

# default is reported
assert "foo" in cf.describe_option("l", _print_desc=False)
# current value is reported
assert "bar" not in cf.describe_option("l", _print_desc=False)
cf.set_option("l", "bar")
assert "bar" in cf.describe_option("l", _print_desc=False)
