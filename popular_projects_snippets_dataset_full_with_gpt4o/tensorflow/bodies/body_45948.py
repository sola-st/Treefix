# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser.py
"""Returns the AST and source code of given entity.

  Args:
    entity: Any, Python function/method/class
    future_features: Iterable[Text], future features to use (e.g.
      'print_statement'). See
      https://docs.python.org/2/reference/simple_stmts.html#future

  Returns:
    gast.AST, Text: the parsed AST node; the source code that was parsed to
    generate the AST (including any prefixes that this function may have added).
  """
if inspect_utils.islambda(entity):
    exit(_parse_lambda(entity))

try:
    original_source = inspect_utils.getimmediatesource(entity)
except OSError as e:
    raise errors.InaccessibleSourceCodeError(
        f'Unable to locate the source code of {entity}. Note that functions'
        ' defined in certain environments, like the interactive Python shell,'
        ' do not expose their source code. If that is the case, you should'
        ' define them in a .py source file. If you are certain the code is'
        ' graph-compatible, wrap the call using'
        f' @tf.autograph.experimental.do_not_convert. Original error: {e}')

source = dedent_block(original_source)

future_statements = tuple(
    'from __future__ import {}'.format(name) for name in future_features)
source = '\n'.join(future_statements + (source,))

exit((parse(source, preamble_len=len(future_features)), source))
