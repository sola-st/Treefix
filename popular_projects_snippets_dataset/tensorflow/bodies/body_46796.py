# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates_test.py
template = """
        foo(bar)
    """
source = parser.parse_expression('[a(b(1))]')
templates.replace_as_expression(template, bar=source)
