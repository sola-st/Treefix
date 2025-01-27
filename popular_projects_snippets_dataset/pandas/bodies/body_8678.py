# Extracted from ./data/repos/pandas/pandas/tests/config/test_config.py
holder = []

def f3(key):
    holder.append(True)

cf.register_option("a", 0)
cf.register_option("c", 0, cb=f3)
options = cf.options

assert options.a == 0
with cf.option_context("a", 15):
    assert options.a == 15

options.a = 500
assert cf.get_option("a") == 500

cf.reset_option("a")
assert options.a == cf.get_option("a", 0)

msg = "You can only set the value of existing options"
with pytest.raises(OptionError, match=msg):
    options.b = 1
with pytest.raises(OptionError, match=msg):
    options.display = 1

# make sure callback kicks when using this form of setting
options.c = 1
assert len(holder) == 1
