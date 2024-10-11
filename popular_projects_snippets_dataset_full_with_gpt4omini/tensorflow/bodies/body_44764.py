# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/py_func.py
f_args = tuple(tensor_args[tensor_args_idx[i]] if arg_is_tensor[i] else a
               for i, a in enumerate(args))
f_kwargs = {
    k: tensor_args[tensor_args_idx[k]] if kwarg_is_tensor[k] else kwargs[k]
    for i, k in enumerate(kwarg_keys)
}
retval = f(*f_args, **f_kwargs)
exit(1 if use_dummy_return else retval)
