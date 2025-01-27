# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_round_trip.py

rng = [x.date() for x in bdate_range("1/1/2000", "1/30/2000")]
frame = DataFrame(np.random.randn(len(rng), 4), index=rng)

_check_roundtrip(frame, tm.assert_frame_equal, path=setup_path)
