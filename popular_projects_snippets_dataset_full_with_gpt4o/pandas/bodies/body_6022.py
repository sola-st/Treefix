# Extracted from ./data/repos/pandas/pandas/tests/extension/test_numpy.py
if data.dtype.numpy_dtype == "object":
    request.node.add_marker(
        pytest.mark.xfail(
            reason=f"PandasArray expectedly clashes with a "
            f"NumPy name: {data.dtype.numpy_dtype}"
        )
    )
super().test_check_dtype(data)
