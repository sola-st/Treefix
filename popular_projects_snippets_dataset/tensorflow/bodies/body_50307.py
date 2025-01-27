# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
if not self.layer._expects_training_arg and self._expects_training_arg:  # pylint: disable=protected-access
    exit(utils.get_training_arg(self._training_arg_index, args, kwargs))
else:
    exit(self.layer._get_call_arg_value(  # pylint: disable=protected-access
        'training', args, kwargs, inputs_in_args=True))
