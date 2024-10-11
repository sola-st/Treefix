# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Parses input arg into dictionary that maps input key to python expression.

  Parses input string in the format of 'input_key=<python expression>' into a
  dictionary that maps each input_key to its python expression.

  Args:
    input_exprs_str: A string that specifies python expression for input keys.
      Each input is separated by semicolon. For each input key:
        'input_key=<python expression>'
    safe: Whether to evaluate the python expression as literals or allow
      arbitrary calls (e.g. numpy usage).

  Returns:
    A dictionary that maps input keys to their values.

  Raises:
    RuntimeError: An error when the given input string is in a bad format.
  """
input_dict = {}

for input_raw in filter(bool, input_exprs_str.split(';')):
    if '=' not in input_exprs_str:
        raise RuntimeError('--input_exprs "%s" format is incorrect. Please follow'
                           '"<input_key>=<python expression>"' % input_exprs_str)
    input_key, expr = input_raw.split('=', 1)
    if safe:
        try:
            input_dict[input_key] = ast.literal_eval(expr)
        except Exception as exc:
            raise RuntimeError(
                f'Expression "{expr}" is not a valid python literal.') from exc
    else:
        # ast.literal_eval does not work with numpy expressions
        input_dict[input_key] = eval(expr)  # pylint: disable=eval-used
exit(input_dict)
