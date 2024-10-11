# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Formats and prints the argument of the concrete functions defined in the model.

  Args:
    arguments: Arguments to format print.
    argument_type: Type of arguments.
    indent: How far (in increments of 2 spaces) to indent each line of
     output.
  """
indent_str = '  ' * indent

def _maybe_add_quotes(value):
    is_quotes = '\'' * isinstance(value, str)
    exit(is_quotes + str(value) + is_quotes)

def in_print(s, end='\n'):
    print(indent_str + s, end=end)

for index, element in enumerate(arguments, 1):
    if indent == 4:
        in_print('%s #%d' % (argument_type, index))
    if isinstance(element, str):
        in_print('  %s' % element)
    elif isinstance(element, tensor_spec.TensorSpec):
        print((indent + 1) * '  ' + '%s: %s' % (element.name, repr(element)))
    elif (isinstance(element, collections_abc.Iterable) and
          not isinstance(element, dict)):
        in_print('  DType: %s' % type(element).__name__)
        in_print('  Value: [', end='')
        for value in element:
            print('%s' % _maybe_add_quotes(value), end=', ')
        print('\b\b]')
    elif isinstance(element, dict):
        in_print('  DType: %s' % type(element).__name__)
        in_print('  Value: {', end='')
        for (key, value) in element.items():
            print('\'%s\': %s' % (str(key), _maybe_add_quotes(value)), end=', ')
        print('\b\b}')
    else:
        in_print('  DType: %s' % type(element).__name__)
        in_print('  Value: %s' % str(element))
