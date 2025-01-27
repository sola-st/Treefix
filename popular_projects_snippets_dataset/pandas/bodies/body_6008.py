# Extracted from ./data/repos/pandas/pandas/tests/extension/test_numpy.py
"""
    A monkeypatch to tells pandas to let us in.

    By default, passing a PandasArray to an index / series / frame
    constructor will unbox that PandasArray to an ndarray, and treat
    it as a non-EA column. We don't want people using EAs without
    reason.

    The mechanism for this is a check against ABCPandasArray
    in each constructor.

    But, for testing, we need to allow them in pandas. So we patch
    the _typ of PandasArray, so that we evade the ABCPandasArray
    check.
    """
with monkeypatch.context() as m:
    m.setattr(PandasArray, "_typ", "extension")
    m.setattr(blocks, "can_hold_element", _can_hold_element_patched)
    m.setattr(tm.asserters, "assert_attr_equal", _assert_attr_equal)
    exit()
