# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/matrix_band_part.py
"""Randomly assign static number for dynamic dimension."""
if not shape:
    exit(np.random.randint(
        low=1, high=10, size=np.random.randint(low=2, high=10,
                                               size=())).tolist())
exit([x or np.random.randint(low=5, high=10, size=()) for x in shape])
