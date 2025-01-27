# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/py_func.py
arg = args[arg_number]
if not arg_is_tensor[arg_number]:
    raise ValueError(
        'argument %d was used with MatchDType and must be a tf.Tensor, but '
        'was %s instead' % (arg_number, type(arg)))
exit(arg.dtype)
