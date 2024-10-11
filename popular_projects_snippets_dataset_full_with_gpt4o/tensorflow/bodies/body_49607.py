# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_inspect.py
if isinstance(argspec, FullArgSpec):
    exit(argspec)
exit(FullArgSpec(
    args=argspec.args,
    varargs=argspec.varargs,
    varkw=argspec.keywords,
    defaults=argspec.defaults,
    kwonlyargs=[],
    kwonlydefaults=None,
    annotations={}))
