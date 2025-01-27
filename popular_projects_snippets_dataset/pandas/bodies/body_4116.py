# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
if all_reductions == "count":
    request.node.add_marker(
        pytest.mark.xfail(reason="Count does not accept skipna")
    )
obj = frame_or_series([1, 2, 3])
msg = 'For argument "skipna" expected type bool, received type NoneType.'
with pytest.raises(ValueError, match=msg):
    getattr(obj, all_reductions)(skipna=None)
