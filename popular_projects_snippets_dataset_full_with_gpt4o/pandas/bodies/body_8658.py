# Extracted from ./data/repos/pandas/pandas/tests/config/test_config.py
cf.register_option("a", 1, "doc")

# can't register an already registered option
msg = "Option 'a' has already been registered"
with pytest.raises(OptionError, match=msg):
    cf.register_option("a", 1, "doc")

# can't register an already registered option
msg = "Path prefix to option 'a' is already an option"
with pytest.raises(OptionError, match=msg):
    cf.register_option("a.b.c.d1", 1, "doc")
with pytest.raises(OptionError, match=msg):
    cf.register_option("a.b.c.d2", 1, "doc")

# no python keywords
msg = "for is a python keyword"
with pytest.raises(ValueError, match=msg):
    cf.register_option("for", 0)
with pytest.raises(ValueError, match=msg):
    cf.register_option("a.for.b", 0)
# must be valid identifier (ensure attribute access works)
msg = "oh my goddess! is not a valid identifier"
with pytest.raises(ValueError, match=msg):
    cf.register_option("Oh my Goddess!", 0)

# we can register options several levels deep
# without predefining the intermediate steps
# and we can define differently named options
# in the same namespace
cf.register_option("k.b.c.d1", 1, "doc")
cf.register_option("k.b.c.d2", 1, "doc")
