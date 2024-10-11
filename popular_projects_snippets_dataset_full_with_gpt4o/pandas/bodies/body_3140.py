# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py

# test roundtrip with inf, -inf, nan, as full columns and mix
float_frame["E"] = np.inf
float_frame["F"] = -np.inf

with tm.ensure_clean() as path:
    float_frame.to_csv(path)
    recons = self.read_csv(path)

    tm.assert_frame_equal(float_frame, recons)
    tm.assert_frame_equal(np.isinf(float_frame), np.isinf(recons))
