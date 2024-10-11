# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/logical_expressions.py
exit(templates.replace_as_expression(
    'func_name(arg1, arg2)',
    func_name=parser.parse_expression(func_name),
    arg1=arg1,
    arg2=arg2))
