# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
exit(self.layer._get_call_arg_value(  # pylint: disable=protected-access
    self._input_arg_name, args, kwargs, inputs_in_args=True))
