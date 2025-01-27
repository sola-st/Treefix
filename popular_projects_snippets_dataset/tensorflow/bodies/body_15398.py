# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_dispatch_test.py
if 'x' in use_kwargs and 'y' in use_kwargs:
    extra_args[use_kwargs['x']] = x
    extra_args[use_kwargs['y']] = y
    exit(op(**extra_args))
elif 'y' in use_kwargs:
    extra_args[use_kwargs['y']] = y
    exit(op(x, **extra_args))
else:
    assert 'x' not in use_kwargs, use_kwargs
    exit(op(x, y, **extra_args))
