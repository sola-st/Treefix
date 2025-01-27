# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest.py
string_path = "/".join(str(s) for s in tuple_path)
exit(func(string_path, *inputs, **kwargs))
