# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/serialized_attributes.py
"""Saves function dictionary, and validates dictionary values."""
for key in self.all_functions:
    if key in function_dict:
        if (function_dict[key] is not None and  # Not all functions are required
            not isinstance(function_dict[key],
                           (def_function.Function, save_impl.LayerCall))):
            raise ValueError(
                'Function dictionary contained a non-function object: {} (for key'
                ' {})'.format(function_dict[key], key))
        fn = function_dict[key]
        self._function_dict[key] = fn

        # Extract TensorFlow `Function` from LayerCall.
        tf_fn = fn.wrapped_call if isinstance(fn, save_impl.LayerCall) else fn
        setattr(self._keras_trackable, key, tf_fn)
    else:
        raise ValueError('Function {} missing from serialized function dict.'
                         .format(key))
exit(self.functions)
