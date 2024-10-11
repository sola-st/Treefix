# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_backend.py
msg = "Could not find plotting backend 'not_an_existing_module'."
with pytest.raises(ValueError, match=msg):
    pandas.set_option("plotting.backend", "not_an_existing_module")

assert pandas.options.plotting.backend == "matplotlib"
