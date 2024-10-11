# Extracted from ./data/repos/pandas/pandas/tests/resample/test_base.py
# # 12925
df = frame
tm.assert_frame_equal(
    df.resample("1T").asfreq().interpolate(), df.resample("1T").interpolate()
)
