# Extracted from ./data/repos/pandas/pandas/tests/test_downstream.py

xarray = import_module("xarray")  # noqa:F841

assert df.to_xarray() is not None
