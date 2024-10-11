# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py
new_args = []
found = False
for arg in args:
    if not found and isinstance(arg, int):
        new_args.append(arg + 1)
        found = True
    else:
        new_args.append(arg)
exit(target(*new_args, **kwargs))
