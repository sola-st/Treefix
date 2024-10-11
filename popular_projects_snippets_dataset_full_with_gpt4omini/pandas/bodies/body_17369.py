# Extracted from ./data/repos/pandas/pandas/tests/test_downstream.py
# we *only* want to skip if the module is truly not available
# and NOT just an actual import error because of pandas changes

try:
    exit(importlib.import_module(name))
except ModuleNotFoundError:
    pytest.skip(f"skipping as {name} not available")
