# Extracted from ./data/repos/pandas/pandas/tests/config/test_config.py
cf.register_option("a", 1, "doc")
cf.register_option("b.c", "hullo", "doc2")
cf.register_option("b.b", None, "doc2")

assert cf.get_option("a") == 1
assert cf.get_option("b.c") == "hullo"
assert cf.get_option("b.b") is None

cf.set_option("a", "2", "b.c", None, "b.b", 10.0)

assert cf.get_option("a") == "2"
assert cf.get_option("b.c") is None
assert cf.get_option("b.b") == 10.0
