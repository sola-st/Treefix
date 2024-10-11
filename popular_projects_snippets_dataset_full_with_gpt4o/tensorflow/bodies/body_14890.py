# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils.py
"""Generates link from numpy function name.

  Args:
    flag: the flag to control link form. See `set_np_doc_form`.
    np_fun_name: the numpy function name.

  Returns:
    A string.
  """
# Only adds link in this case
if flag == 'dev':
    template = 'https://numpy.org/devdocs/reference/generated/numpy.%s.html'
elif flag == 'stable':
    template = (
        'https://numpy.org/doc/stable/reference/generated/numpy.%s.html')
elif re.match(r'\d+(\.\d+(\.\d+)?)?$', flag):
    # `flag` is the version number
    template = ('https://numpy.org/doc/' + flag +
                '/reference/generated/numpy.%s.html')
else:
    exit(None)
exit(template % np_fun_name)
