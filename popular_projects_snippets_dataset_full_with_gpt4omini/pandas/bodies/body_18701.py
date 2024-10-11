# Extracted from ./data/repos/pandas/pandas/conftest.py
parser.addoption("--skip-slow", action="store_true", help="skip slow tests")
parser.addoption("--skip-network", action="store_true", help="skip network tests")
parser.addoption("--skip-db", action="store_true", help="skip db tests")
parser.addoption(
    "--run-high-memory", action="store_true", help="run high memory tests"
)
parser.addoption("--only-slow", action="store_true", help="run only slow tests")
parser.addoption(
    "--strict-data-files",
    action="store_true",
    help="Fail if a test is skipped for missing data file.",
)
