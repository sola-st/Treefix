# Extracted from ./data/repos/pandas/pandas/tests/extension/test_numpy.py
if data.dtype.numpy_dtype == object:
    mark = pytest.mark.xfail(reason="Dimension mismatch in np.concatenate")
    request.node.add_marker(mark)

super().test_insert(data)
