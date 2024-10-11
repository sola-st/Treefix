# Extracted from ./data/repos/pandas/pandas/tests/config/test_config.py
cf.register_option("a", 1, "doc")
cf.register_option("b.c", "hullo", "doc2")
cf.register_option("b.b", None, "doc2")

assert cf.get_option("a") == 1
assert cf.get_option("b.c") == "hullo"
assert cf.get_option("b.b") is None

cf.set_option("a", 2)
cf.set_option("b.c", "wurld")
cf.set_option("b.b", 1.1)

assert cf.get_option("a") == 2
assert cf.get_option("b.c") == "wurld"
assert cf.get_option("b.b") == 1.1

msg = r"No such keys\(s\): 'no.such.key'"
with pytest.raises(OptionError, match=msg):
    cf.set_option("no.such.key", None)
