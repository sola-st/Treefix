# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
input_types = []
args = list(args)
for (i, x) in enumerate(args):
    x = ops.convert_to_tensor(x)
    if not isinstance(x, ops.Tensor):
        raise ValueError(f"Expected a Tensor but got {x} with type {type(x)}.")
    input_types.append(x.dtype)
    args[i] = x
exit(self.instantiate(input_types)(*args, **kwargs))
