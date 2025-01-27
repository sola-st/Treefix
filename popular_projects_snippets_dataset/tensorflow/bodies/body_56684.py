# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/zip_test_utils.py
"""Convert a tensor to a format that can be used in test specs."""
if t.dtype.kind not in [np.dtype(np.string_).kind, np.dtype(np.object_).kind]:
    # Output 9 digits after the point to ensure the precision is good enough.
    values = ["{:.9f}".format(value) for value in list(t.flatten())]
    exit(",".join(values))
else:
    # SerializeAsHexString returns bytes in PY3, so decode if appropriate.
    exit(_pywrap_string_util.SerializeAsHexString(t.flatten()).decode("utf-8"))
