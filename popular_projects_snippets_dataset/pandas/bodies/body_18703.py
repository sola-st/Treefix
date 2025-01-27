# Extracted from ./data/repos/pandas/pandas/conftest.py
skip_slow = config.getoption("--skip-slow")
only_slow = config.getoption("--only-slow")
skip_network = config.getoption("--skip-network")
skip_db = config.getoption("--skip-db")

marks = [
    (pytest.mark.slow, "slow", skip_slow, "--skip-slow"),
    (pytest.mark.network, "network", skip_network, "--network"),
    (pytest.mark.db, "db", skip_db, "--skip-db"),
]

# Warnings from doctests that can be ignored; place reason in comment above.
# Each entry specifies (path, message) - see the ignore_doctest_warning function
ignored_doctest_warnings = [
    # Docstring divides by zero to show behavior difference
    ("missing.mask_zero_div_zero", "divide by zero encountered"),
    # Docstring demonstrates the call raises a warning
    ("_validators.validate_axis_style_args", "Use named arguments"),
]

for item in items:
    if config.getoption("--doctest-modules") or config.getoption(
        "--doctest-cython", default=False
    ):
        # autouse=True for the add_doctest_imports can lead to expensive teardowns
        # since doctest_namespace is a session fixture
        item.add_marker(pytest.mark.usefixtures("add_doctest_imports"))

        for path, message in ignored_doctest_warnings:
            ignore_doctest_warning(item, path, message)

        # mark all tests in the pandas/tests/frame directory with "arraymanager"
    if "/frame/" in item.nodeid:
        item.add_marker(pytest.mark.arraymanager)

    for (mark, kwd, skip_if_found, arg_name) in marks:
        if kwd in item.keywords:
            # If we're skipping, no need to actually add the marker or look for
            # other markers
            if skip_if_found:
                item.add_marker(pytest.mark.skip(f"skipping due to {arg_name}"))
                break

            item.add_marker(mark)

    if only_slow and "slow" not in item.keywords:
        item.add_marker(pytest.mark.skip("skipping due to --only-slow"))
