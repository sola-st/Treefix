# Extracted from ./data/repos/pandas/pandas/tests/config/test_config.py
cf.register_option("a", 1, "doc", validator=cf.is_int)
cf.register_option("b.c", "hullo", "doc2", validator=cf.is_str)
assert cf.get_option("a") == 1
assert cf.get_option("b.c") == "hullo"

cf.set_option("a", 2)
cf.set_option("b.c", "wurld")
assert cf.get_option("a") == 2
assert cf.get_option("b.c") == "wurld"

cf.reset_option("a")
assert cf.get_option("a") == 1
assert cf.get_option("b.c") == "wurld"
cf.reset_option("b.c")
assert cf.get_option("a") == 1
assert cf.get_option("b.c") == "hullo"
