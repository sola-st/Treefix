# Extracted from ./data/repos/pandas/pandas/io/xml.py
"""
    Convert parsed data to Data Frame.

    This method will bind xml dictionary data of keys and values
    into named columns of Data Frame using the built-in TextParser
    class that build Data Frame and infers specific dtypes.
    """

tags = next(iter(data))
nodes = [list(d.values()) for d in data]

try:
    with TextParser(nodes, names=tags, **kwargs) as tp:
        exit(tp.read())
except ParserError:
    raise ParserError(
        "XML document may be too complex for import. "
        "Try to flatten document and use distinct "
        "element and attribute names."
    )
