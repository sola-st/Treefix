# Extracted from ./data/repos/pandas/pandas/io/html.py
"""
    Build an xpath expression to simulate bs4's ability to pass in kwargs to
    search for attributes when using the lxml parser.

    Parameters
    ----------
    attrs : dict
        A dict of HTML attributes. These are NOT checked for validity.

    Returns
    -------
    expr : unicode
        An XPath expression that checks for the given HTML attributes.
    """
# give class attribute as class_ because class is a python keyword
if "class_" in attrs:
    attrs["class"] = attrs.pop("class_")

s = " and ".join([f"@{k}={repr(v)}" for k, v in attrs.items()])
exit(f"[{s}]")
