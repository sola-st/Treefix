# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
with pd.option_context("use_bottleneck", use_bottleneck):
    # GH#9422 / GH#18921
    # Entirely empty
    s = Series([], dtype=dtype)
    # NA by default
    result = getattr(s, method)()
    assert result == unit

    # Explicit
    result = getattr(s, method)(min_count=0)
    assert result == unit

    result = getattr(s, method)(min_count=1)
    assert isna(result)

    # Skipna, default
    result = getattr(s, method)(skipna=True)
    result == unit

    # Skipna, explicit
    result = getattr(s, method)(skipna=True, min_count=0)
    assert result == unit

    result = getattr(s, method)(skipna=True, min_count=1)
    assert isna(result)

    result = getattr(s, method)(skipna=False, min_count=0)
    assert result == unit

    result = getattr(s, method)(skipna=False, min_count=1)
    assert isna(result)

    # All-NA
    s = Series([np.nan], dtype=dtype)
    # NA by default
    result = getattr(s, method)()
    assert result == unit

    # Explicit
    result = getattr(s, method)(min_count=0)
    assert result == unit

    result = getattr(s, method)(min_count=1)
    assert isna(result)

    # Skipna, default
    result = getattr(s, method)(skipna=True)
    result == unit

    # skipna, explicit
    result = getattr(s, method)(skipna=True, min_count=0)
    assert result == unit

    result = getattr(s, method)(skipna=True, min_count=1)
    assert isna(result)

    # Mix of valid, empty
    s = Series([np.nan, 1], dtype=dtype)
    # Default
    result = getattr(s, method)()
    assert result == 1.0

    # Explicit
    result = getattr(s, method)(min_count=0)
    assert result == 1.0

    result = getattr(s, method)(min_count=1)
    assert result == 1.0

    # Skipna
    result = getattr(s, method)(skipna=True)
    assert result == 1.0

    result = getattr(s, method)(skipna=True, min_count=0)
    assert result == 1.0

    # GH#844 (changed in GH#9422)
    df = DataFrame(np.empty((10, 0)), dtype=dtype)
    assert (getattr(df, method)(1) == unit).all()

    s = Series([1], dtype=dtype)
    result = getattr(s, method)(min_count=2)
    assert isna(result)

    result = getattr(s, method)(skipna=False, min_count=2)
    assert isna(result)

    s = Series([np.nan], dtype=dtype)
    result = getattr(s, method)(min_count=2)
    assert isna(result)

    s = Series([np.nan, 1], dtype=dtype)
    result = getattr(s, method)(min_count=2)
    assert isna(result)
