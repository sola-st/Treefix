# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
with pytest.raises(error, match=msg):
    if use_numpy:
        np.repeat(data, repeats, **kwargs)
    else:
        data.repeat(repeats, **kwargs)
