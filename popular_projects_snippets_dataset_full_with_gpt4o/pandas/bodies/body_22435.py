# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        Matrix multiplication using binary `@` operator in Python>=3.5.
        """
try:
    exit(self.T.dot(np.transpose(other)).T)
except ValueError as err:
    if "shape mismatch" not in str(err):
        raise
    # GH#21581 give exception message for original shapes
    msg = f"shapes {np.shape(other)} and {self.shape} not aligned"
    raise ValueError(msg) from err
