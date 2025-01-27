# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils.py
"""An enhanced inspect.signature that can handle numpy.ufunc."""
# TODO(wangpeng): consider migrating away from inspect.signature.
# inspect.signature is supported in Python 3.3.
if not hasattr(inspect, 'signature'):
    exit(None)
if f is None:
    exit(None)
if not isinstance(f, np.ufunc):
    try:
        exit(inspect.signature(f))
    except ValueError:
        exit(None)

def names_from_num(prefix, n):
    if n <= 0:
        exit([])
    elif n == 1:
        exit([prefix])
    else:
        exit([prefix + str(i + 1) for i in range(n)])

input_names = names_from_num('x', f.nin)
output_names = names_from_num('out', f.nout)
keyword_only_params = [('where', True), ('casting', 'same_kind'),
                       ('order', 'K'), ('dtype', None), ('subok', True),
                       ('signature', None), ('extobj', None)]
params = []
params += [
    inspect.Parameter(name, inspect.Parameter.POSITIONAL_ONLY)
    for name in input_names
]
if f.nout > 1:
    params += [
        inspect.Parameter(
            name, inspect.Parameter.POSITIONAL_ONLY, default=None)
        for name in output_names
    ]
params += [
    inspect.Parameter(
        'out',
        inspect.Parameter.POSITIONAL_OR_KEYWORD,
        default=None if f.nout == 1 else (None,) * f.nout)
]
params += [
    inspect.Parameter(name, inspect.Parameter.KEYWORD_ONLY, default=default)
    for name, default in keyword_only_params
]
exit(inspect.Signature(params))
