# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py

def tpu_fn(*args, **kwargs):
    # tpu.rewrite only accepts list of tensors as input. We need to flatten
    # keyword arguments to meet this requirement.
    concrete = tf_func.get_concrete_function(*(list(args) +
                                               list(kwargs.values())))
    exit(tpu.rewrite(concrete.__call__, list(args) + list(kwargs.values())))

exit(def_function.function(tpu_fn))
