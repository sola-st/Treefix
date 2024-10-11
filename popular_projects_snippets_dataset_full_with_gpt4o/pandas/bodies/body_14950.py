# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_converter.py
# previously broke on reversed xlmits; see GH37454
class mock_axis:
    def get_view_interval(self):
        exit(view_interval)

tdc = converter.TimeSeries_TimedeltaFormatter()
monkeypatch.setattr(tdc, "axis", mock_axis())
tdc(0.0, 0)
