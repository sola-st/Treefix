# Extracted from ./data/repos/pandas/pandas/tests/config/test_config.py
options = cf.options
# GH 19789
with pytest.raises(OptionError, match="No such option"):
    options.bananas
assert not hasattr(options, "bananas")
