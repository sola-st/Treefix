# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
if isinstance(layer.call, (def_function.Function)):
    exit(layer.call.python_function)
exit(layer.call)
