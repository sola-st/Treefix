# Extracted from ./data/repos/pandas/pandas/tests/generic/test_generic.py
box = frame_or_series
obj = box(dtype=object)
values = box._AXIS_TO_AXIS_NUMBER.keys()
for v in values:
    assert obj._get_axis_number(v) == box._get_axis_number(v)
    assert obj._get_axis_name(v) == box._get_axis_name(v)
    assert obj._get_block_manager_axis(v) == box._get_block_manager_axis(v)
