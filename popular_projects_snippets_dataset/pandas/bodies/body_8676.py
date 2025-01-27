# Extracted from ./data/repos/pandas/pandas/tests/config/test_config.py
def eq(val):
    assert cf.get_option("a") == val

cf.register_option("a", 0)
eq(0)
with cf.option_context("a", 15):
    eq(15)
    with cf.option_context("a", 25):
        eq(25)
    eq(15)
eq(0)

cf.set_option("a", 17)
eq(17)

# Test that option_context can be used as a decorator too (#34253).
@cf.option_context("a", 123)
def f():
    eq(123)

f()
