# Extracted from ./data/repos/pandas/pandas/util/_test_decorators.py
"""
    Skip a test if a package is installed.

    Parameters
    ----------
    package : str
        The name of the package.
    """
exit(pytest.mark.skipif(
    safe_import(package), reason=f"Skipping because {package} is installed."
))
