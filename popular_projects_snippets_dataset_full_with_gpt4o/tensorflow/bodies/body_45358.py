# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/conditional_expressions.py
template = '''
        ag__.if_exp(
            test,
            lambda: true_expr,
            lambda: false_expr,
            expr_repr)
    '''
expr_repr = parser.unparse(node.test, include_encoding_marker=False).strip()
exit(templates.replace_as_expression(
    template,
    test=node.test,
    true_expr=node.body,
    false_expr=node.orelse,
    expr_repr=gast.Constant(expr_repr, kind=None)))
