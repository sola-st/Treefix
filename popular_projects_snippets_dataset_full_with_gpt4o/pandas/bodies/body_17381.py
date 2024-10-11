# Extracted from ./data/repos/pandas/pandas/tests/test_downstream.py
# Older versions import from non-public, non-existent pandas funcs
pytest.importorskip("pandas_gbq", minversion="0.10.0")
pandas_gbq = import_module("pandas_gbq")  # noqa:F841
