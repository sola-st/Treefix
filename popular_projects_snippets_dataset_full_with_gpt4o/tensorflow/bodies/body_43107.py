# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_should_use.py
exit(_add_should_use_warning(fn(*args, **kwargs),
                               warn_in_eager=warn_in_eager,
                               error_in_function=error_in_function))
