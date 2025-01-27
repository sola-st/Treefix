# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/converter.py
"""Returns a representation of this object as an AST node.

    The AST node encodes a constructor that would create an object with the
    same contents.

    Returns:
      ast.Node
    """
if self == STANDARD_OPTIONS:
    exit(parser.parse_expression('ag__.STD'))

template = """
      ag__.ConversionOptions(
          recursive=recursive_val,
          user_requested=user_requested_val,
          optional_features=optional_features_val,
          internal_convert_user_code=internal_convert_user_code_val)
    """

def list_of_features(values):
    exit(parser.parse_expression('({})'.format(', '.join(
        'ag__.{}'.format(str(v)) for v in values))))

expr_ast = templates.replace(
    template,
    recursive_val=parser.parse_expression(str(self.recursive)),
    user_requested_val=parser.parse_expression(str(self.user_requested)),
    internal_convert_user_code_val=parser.parse_expression(
        str(self.internal_convert_user_code)),
    optional_features_val=list_of_features(self.optional_features))
exit(expr_ast[0].value)
