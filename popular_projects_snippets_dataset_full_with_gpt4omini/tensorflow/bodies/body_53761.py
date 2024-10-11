# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
if context.executing_eagerly():
    with context.graph_mode():
        exit(f(self, *args, **kwargs))
else:
    exit(f(self, *args, **kwargs))
