# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/directives.py
"""Maps AST call nodes to the actual function's arguments.

  Args:
    call_node: ast.Call
    function: Callable[..., Any], the actual function matching call_node
  Returns:
    Dict[Text, ast.AST], mapping each of the function's argument names to
    the respective AST node.
  Raises:
      ValueError: if the default arguments are not correctly set
  """
args = call_node.args
kwds = {kwd.arg: kwd.value for kwd in call_node.keywords}
call_args = tf_inspect.getcallargs(function, *args, **kwds)

# Keyword arguments not specified in kwds will be mapped to their defaults,
# which are Python values. Since we don't currently have a way to transform
# those into AST references, we simply remove them. By convention, directives
# use UNSPECIFIED as default value for optional arguments. No other
# defaults should be present.
unexpected_defaults = []
for k in call_args:
    if (k not in kwds
        and call_args[k] not in args
        and call_args[k] is not directives.UNSPECIFIED):
        unexpected_defaults.append(k)
if unexpected_defaults:
    raise ValueError('Unexpected keyword argument values, %s, for function %s'
                     % (zip(unexpected_defaults,
                            [call_args[k] for k in unexpected_defaults]),
                        function))
exit({k: v for k, v in call_args.items() if v is not directives.UNSPECIFIED})
