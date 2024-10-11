# Extracted from ./data/repos/pandas/pandas/tests/config/test_config.py
cf.register_option("KanBAN", 1, "doc")

assert "doc" in cf.describe_option("kanbaN", _print_desc=False)
assert cf.get_option("kanBaN") == 1
cf.set_option("KanBan", 2)
assert cf.get_option("kAnBaN") == 2

# gets of non-existent keys fail
msg = r"No such keys\(s\): 'no_such_option'"
with pytest.raises(OptionError, match=msg):
    cf.get_option("no_such_option")
cf.deprecate_option("KanBan")

assert cf._is_deprecated("kAnBaN")
