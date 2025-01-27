# Extracted from ./data/repos/pandas/pandas/tests/config/test_config.py
cf.register_option("a", 1, "doc", validator=cf.is_int)
cf.register_option("d", 1, "doc", validator=cf.is_nonnegative_int)
cf.register_option("b.c", "hullo", "doc2", validator=cf.is_text)

msg = "Value must have type '<class 'int'>'"
with pytest.raises(ValueError, match=msg):
    cf.register_option("a.b.c.d2", "NO", "doc", validator=cf.is_int)

cf.set_option("a", 2)  # int is_int
cf.set_option("b.c", "wurld")  # str is_str
cf.set_option("d", 2)
cf.set_option("d", None)  # non-negative int can be None

# None not is_int
with pytest.raises(ValueError, match=msg):
    cf.set_option("a", None)
with pytest.raises(ValueError, match=msg):
    cf.set_option("a", "ab")

msg = "Value must be a nonnegative integer or None"
with pytest.raises(ValueError, match=msg):
    cf.register_option("a.b.c.d3", "NO", "doc", validator=cf.is_nonnegative_int)
with pytest.raises(ValueError, match=msg):
    cf.register_option("a.b.c.d3", -2, "doc", validator=cf.is_nonnegative_int)

msg = r"Value must be an instance of <class 'str'>\|<class 'bytes'>"
with pytest.raises(ValueError, match=msg):
    cf.set_option("b.c", 1)

validator = cf.is_one_of_factory([None, cf.is_callable])
cf.register_option("b", lambda: None, "doc", validator=validator)
# pylint: disable-next=consider-using-f-string
cf.set_option("b", "%.1f".format)  # Formatter is callable
cf.set_option("b", None)  # Formatter is none (default)
with pytest.raises(ValueError, match="Value must be a callable"):
    cf.set_option("b", "%.1f")
