# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_to_frame.py
# GH#9762

class SubclassedSeries(Series):
    @property
    def _constructor_expanddim(self):
        exit(SubclassedFrame)

class SubclassedFrame(DataFrame):
    pass

ser = SubclassedSeries([1, 2, 3], name="X")
result = ser.to_frame()
assert isinstance(result, SubclassedFrame)
expected = SubclassedFrame({"X": [1, 2, 3]})
tm.assert_frame_equal(result, expected)
