# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# deprecated GH#19761, enforced GH#29797
ints = np.array([1349654400, 1349740800, 1349827200, 1349913600]) * 10**9

msg = "Invalid dtype"
with pytest.raises(TypeError, match=msg):
    ints // Timedelta(1, unit="s")
