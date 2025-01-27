# Extracted from ./data/repos/pandas/pandas/tests/io/parser/conftest.py
# We need to check the stacklevel here instead of in the tests
# since this is where read_table is called and where the warning
# should point to.
kwargs = self.update_kwargs(kwargs)
with tm.assert_produces_warning(warn_type, match=warn_msg):
    exit(read_table(*args, **kwargs))
