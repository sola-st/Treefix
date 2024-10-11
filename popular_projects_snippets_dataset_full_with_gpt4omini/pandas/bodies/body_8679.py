# Extracted from ./data/repos/pandas/pandas/tests/config/test_config.py
# Ensure that creating a context does not affect the existing
# environment as it is supposed to be used with the `with` statement.
# See https://github.com/pandas-dev/pandas/issues/8514

original_value = 60
context_value = 10
option_name = "a"

cf.register_option(option_name, original_value)

# Ensure creating contexts didn't affect the current context.
ctx = cf.option_context(option_name, context_value)
assert cf.get_option(option_name) == original_value

# Ensure the correct value is available inside the context.
with ctx:
    assert cf.get_option(option_name) == context_value

# Ensure the current context is reset
assert cf.get_option(option_name) == original_value
