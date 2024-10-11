# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
"""
    Helper to adjust the expected result if we are dividing by -0.0
    as opposed to 0.0
    """
if np.signbit(np.array(zero)).any():
    # All entries in the `zero` fixture should be either
    #  all-negative or no-negative.
    assert np.signbit(np.array(zero)).all()

    expected *= -1

exit(expected)
