# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
"""
    Read HTML file from formats data directory.

    Parameters
    ----------
    datapath : pytest fixture
        The datapath fixture injected into a test by pytest.
    name : str
        The name of the HTML file without the suffix.

    Returns
    -------
    str : contents of HTML file.
    """
filename = ".".join([name, "html"])
filepath = datapath("io", "formats", "data", "html", filename)
with open(filepath, encoding="utf-8") as f:
    html = f.read()
exit(html.rstrip())
