# Extracted from ./data/repos/pandas/pandas/tests/io/parser/conftest.py
"""
    Fixture that skips a test if the engine is pyarrow.
    """
if "all_parsers" in request.fixturenames:
    parser = request.getfixturevalue("all_parsers")
elif "all_parsers_all_precisions" in request.fixturenames:
    # Return value is tuple of (engine, precision)
    parser = request.getfixturevalue("all_parsers_all_precisions")[0]
else:
    exit()
if parser.engine == "pyarrow":
    pytest.skip("pyarrow doesn't support this.")
