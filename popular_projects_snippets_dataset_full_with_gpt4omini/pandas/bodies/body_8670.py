# Extracted from ./data/repos/pandas/pandas/tests/config/test_config.py
# we can deprecate non-existent options
cf.deprecate_option("foo")

assert cf._is_deprecated("foo")
with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    with pytest.raises(KeyError, match="No such keys.s.: 'foo'"):
        cf.get_option("foo")
    assert len(w) == 1  # should have raised one warning
    assert "deprecated" in str(w[-1])  # we get the default message

cf.register_option("a", 1, "doc", validator=cf.is_int)
cf.register_option("b.c", "hullo", "doc2")
cf.register_option("foo", "hullo", "doc2")

cf.deprecate_option("a", removal_ver="nifty_ver")
with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    cf.get_option("a")

    assert len(w) == 1  # should have raised one warning
    assert "eprecated" in str(w[-1])  # we get the default message
    assert "nifty_ver" in str(w[-1])  # with the removal_ver quoted

    msg = "Option 'a' has already been defined as deprecated"
    with pytest.raises(OptionError, match=msg):
        cf.deprecate_option("a")

cf.deprecate_option("b.c", "zounds!")
with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    cf.get_option("b.c")

    assert len(w) == 1  # should have raised one warning
    assert "zounds!" in str(w[-1])  # we get the custom message

# test rerouting keys
cf.register_option("d.a", "foo", "doc2")
cf.register_option("d.dep", "bar", "doc2")
assert cf.get_option("d.a") == "foo"
assert cf.get_option("d.dep") == "bar"

cf.deprecate_option("d.dep", rkey="d.a")  # reroute d.dep to d.a
with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    assert cf.get_option("d.dep") == "foo"

    assert len(w) == 1  # should have raised one warning
    assert "eprecated" in str(w[-1])  # we get the custom message

with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    cf.set_option("d.dep", "baz")  # should overwrite "d.a"

    assert len(w) == 1  # should have raised one warning
    assert "eprecated" in str(w[-1])  # we get the custom message

with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    assert cf.get_option("d.dep") == "baz"

    assert len(w) == 1  # should have raised one warning
    assert "eprecated" in str(w[-1])  # we get the custom message
