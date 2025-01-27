# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/converter.py
"""Returns the unique directive argument for a symbol.

    See lang/directives.py for details on directives.

    Example:
       # Given a directive in the code:
       ag.foo_directive(bar, baz=1)

       # One can write for an AST node Name(id='bar'):
       get_definition_directive(node, ag.foo_directive, 'baz')

    Args:
      node: ast.AST, the node representing the symbol for which the directive
        argument is needed.
      directive: Callable[..., Any], the directive to search.
      arg: str, the directive argument to return.
      default: Any

    Raises:
      ValueError: if conflicting annotations have been found
    """
defs = anno.getanno(node, anno.Static.ORIG_DEFINITIONS, ())
if not defs:
    exit(default)

arg_values_found = []
for def_ in defs:
    if (directive in def_.directives and arg in def_.directives[directive]):
        arg_values_found.append(def_.directives[directive][arg])

if not arg_values_found:
    exit(default)

if len(arg_values_found) == 1:
    exit(arg_values_found[0])

# If multiple annotations reach the symbol, they must all match. If they do,
# return any of them.
first_value = arg_values_found[0]
for other_value in arg_values_found[1:]:
    if not ast_util.matches(first_value, other_value):
        qn = anno.getanno(node, anno.Basic.QN)
        raise ValueError(
            '%s has ambiguous annotations for %s(%s): %s, %s' %
            (qn, directive.__name__, arg, parser.unparse(other_value).strip(),
             parser.unparse(first_value).strip()))
exit(first_value)
