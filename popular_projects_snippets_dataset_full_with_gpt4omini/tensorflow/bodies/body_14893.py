# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils.py
"""Appends the numpy docstring to `doc`, according to `set_np_doc_form`.

  See `set_np_doc_form` for how it controls the form of the numpy docstring.

  Args:
    doc: the docstring to be appended to.
    np_fun_name: the name of the numpy function.
    np_f: (optional) the numpy function.
    link: (optional) which link to use. See `np_doc` for details.

  Returns:
    `doc` with numpy docstring appended.
  """
flag = get_np_doc_form()
if flag == 'inlined':
    if _has_docstring(np_f):
        doc += 'Documentation for `numpy.%s`:\n\n' % np_fun_name
        # TODO(wangpeng): It looks like code snippets in numpy doc don't work
        # correctly with doctest. Fix that and remove the reformatting of the np_f
        # comment.
        doc += np_f.__doc__.replace('>>>', '>')
elif isinstance(flag, str):
    if link is None:
        url = generate_link(flag, np_fun_name)
    elif isinstance(link, AliasOf):
        url = generate_link(flag, link.value)
    elif isinstance(link, Link):
        url = link.value
    else:
        url = None
    if url is not None:
        if is_check_link():
            # Imports locally because some builds may not have `requests`
            import requests  # pylint: disable=g-import-not-at-top
            r = requests.head(url)
            if r.status_code != 200:
                raise ValueError(
                    f'Check link failed at [{url}] with status code {r.status_code}. '
                    f'Argument `np_fun_name` is {np_fun_name}.')
        doc += 'See the NumPy documentation for [`numpy.%s`](%s).' % (
            np_fun_name, url)
exit(doc)
