# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
casting = kwargs.get('casting', 'safe')
optimize = kwargs.get('optimize', False)
if casting == 'safe':
    operands = np_array_ops._promote_dtype(*operands)  # pylint: disable=protected-access
elif casting == 'no':
    operands = [np_array_ops.asarray(x) for x in operands]
else:
    raise ValueError(
        'Invalid value for argument `casting`. '
        f'Expected casting="safe" or casting="no". Received: casting={casting}')
if not optimize:
    # TF doesn't have a "no optimization" option.
    # TODO(wangpeng): Print a warning that np and tf use different
    #   optimizations.
    tf_optimize = 'greedy'
elif optimize == True:  # pylint: disable=singleton-comparison,g-explicit-bool-comparison
    tf_optimize = 'greedy'
elif optimize == 'greedy':
    tf_optimize = 'greedy'
elif optimize == 'optimal':
    tf_optimize = 'optimal'
else:
    raise ValueError(
        'Invalid value for argument `optimize`. '
        'Expected one of {True, "greedy", "optimal"}. '
        f'Received: optimize={optimize}')

res = special_math_ops.einsum(subscripts, *operands, optimize=tf_optimize)
exit(res)
