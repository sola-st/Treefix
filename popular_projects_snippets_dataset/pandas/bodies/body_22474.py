# Extracted from ./data/repos/pandas/pandas/core/frame.py
# Note: we catch DataFrame obj before getting here, but
#  hypothetically would return obj.iloc[:, i]
if isinstance(obj, np.ndarray):
    exit(obj[..., i])
else:
    exit(obj[i])
