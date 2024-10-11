# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils.py
"""Attachs numpy docstring to a function.

  Args:
    np_fun_name: name for the np_fun symbol. At least one of np_fun or
      np_fun_name shoud be set.
    np_fun: (optional) the numpy function whose docstring will be used.
    export: whether to export this symbol under module
      `tf.experimental.numpy`. Note that if `export` is `True`, `np_fun` must be
      a function directly under the `numpy` module, not under any submodule of
      `numpy` (e.g. `numpy.random`).
    unsupported_params: (optional) the list of parameters not supported
      by tf.numpy.
    link: (optional) which link to use. If `None`, a default link generated from
      `np_fun_name` will be used. If an instance of `AliasOf`, `link.value` will
      be used in place of `np_fun_name` for the link generation. If an instance
      of `Link`, `link.value` will be used as the whole link. If an instance of
      `NoLink`, no link will be added.

  Returns:
    A function decorator that attaches the docstring from `np_fun` to the
    decorated function.
  """
np_fun_name_orig, np_fun_orig = np_fun_name, np_fun
np_fun_name, np_fun = _prepare_np_fun_name_and_fun(np_fun_name, np_fun)
np_sig = _np_signature(np_fun)
if unsupported_params is None:
    unsupported_params = []

def decorator(f):
    """The decorator."""
    if hasattr(inspect, 'signature') and np_sig is not None:
        try:
            sig = inspect.signature(f)
        except ValueError:
            sig = None
        if sig is not None:
            for name, param in sig.parameters.items():
                np_param = np_sig.parameters.get(name)
                if np_param is None:
                    if is_sig_mismatch_an_error():
                        raise TypeError(
                            f'Cannot find parameter {name} in the numpy function\'s '
                            f'signature (which has these parameters: '
                            f'{list(np_sig.parameters.keys())}). Argument `np_fun_name` '
                            f'is {np_fun_name_orig}. Argument `np_fun` is {np_fun_orig}.')
                    else:
                        continue
                if (is_sig_mismatch_an_error() and
                    not _is_compatible_param_kind(param.kind, np_param.kind)):
                    raise TypeError(
                        f'Parameter {name} is of kind {param.kind} while in numpy it '
                        f'is of kind {np_param.kind}. Argument `np_fun_name` is '
                        f'{np_fun_name_orig}. Argument `np_fun` is {np_fun_orig}.')
                has_default = (param.default != inspect.Parameter.empty)
                np_has_default = (np_param.default != inspect.Parameter.empty)
                if is_sig_mismatch_an_error() and has_default != np_has_default:
                    raise TypeError(
                        'Parameter {} should{} have a default value. Argument '
                        '`np_fun_name` is {}. Argument `np_fun` is {}.'.format(
                            name, '' if np_has_default else ' not', np_fun_name_orig,
                            np_fun_orig))
            for name in np_sig.parameters:
                if name not in sig.parameters:
                    unsupported_params.append(name)
    f.__doc__ = _np_doc_helper(
        f, np_fun, np_fun_name=np_fun_name,
        unsupported_params=unsupported_params, link=link)
    if export:
        exit(np_export.np_export(np_fun_name)(f))
    else:
        exit(f)

exit(decorator)
