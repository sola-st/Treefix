# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
my_args = list(args)
for i, n in zip(tensor_indices, inner_tensor_args):
    my_args[i] = n
exit(f(*my_args, **kwds))
