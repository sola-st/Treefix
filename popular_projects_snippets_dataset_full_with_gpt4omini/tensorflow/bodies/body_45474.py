# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/logical_expressions.py
exit(templates.replace_as_expression(
    'func_name(arg)', func_name=parser.parse_expression(func_name), arg=arg))
