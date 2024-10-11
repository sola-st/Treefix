# Extracted from ./data/repos/pandas/pandas/tests/frame/test_validate.py
msg = 'For argument "inplace" expected type bool'
kwargs = {"inplace": inplace}

if func == "query":
    kwargs["expr"] = "a > b"
elif func == "eval":
    kwargs["expr"] = "a + b"
elif func == "set_index":
    kwargs["keys"] = ["a"]
elif func == "sort_values":
    kwargs["by"] = ["a"]

with pytest.raises(ValueError, match=msg):
    getattr(dataframe, func)(**kwargs)
