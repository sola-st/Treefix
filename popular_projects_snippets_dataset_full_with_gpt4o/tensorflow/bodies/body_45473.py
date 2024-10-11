# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/logical_expressions.py
template = templates.replace_as_expression(
    'arg1 is arg2',  # Note: `is` will be replaced with `op` below.
    arg1=arg1,
    arg2=arg2)
template.ops[0] = op
exit(template)
