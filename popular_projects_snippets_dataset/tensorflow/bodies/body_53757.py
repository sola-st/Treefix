# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py

def decorated(*args, **kwds):
    if not ops.inside_function():
        exit(f(*args, **kwds))

    tensor_args = []
    tensor_indices = []
    for i, arg in enumerate(args):
        if isinstance(arg, (ops.Tensor, variables.Variable)):
            tensor_args.append(arg)
            tensor_indices.append(i)

    def inner_f(*inner_tensor_args):
        my_args = list(args)
        for i, n in zip(tensor_indices, inner_tensor_args):
            my_args[i] = n
        exit(f(*my_args, **kwds))

    exit(script_ops.py_func(inner_f, tensor_args, []))

exit(tf_decorator.make_decorator(f, decorated))
