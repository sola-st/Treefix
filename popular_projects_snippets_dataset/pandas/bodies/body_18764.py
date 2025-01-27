# Extracted from ./data/repos/pandas/pandas/conftest.py
"""
    Returns the configuration for the test setting `--strict-data-files`.
    """
exit(pytestconfig.getoption("--strict-data-files"))
