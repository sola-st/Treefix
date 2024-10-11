# Extracted from ./data/repos/pandas/pandas/tests/window/test_apply.py
with pytest.raises(ValueError, match="cython engine does not accept engine_kwargs"):
    Series(range(1)).rolling(1).apply(
        lambda x: x, engine="cython", engine_kwargs={"nopython": False}
    )
