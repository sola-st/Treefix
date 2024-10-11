# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
variable = getter(*args, **kwargs)
if ops.executing_eagerly_outside_functions():
    trainable = variable.trainable
else:
    trainable = (
        variable in tf_variables.trainable_variables() or
        (base_layer_utils.is_split_variable(variable) and
         list(variable)[0] in tf_variables.trainable_variables()))
if trainable and all(variable is not v for v in self._trainable_weights):
    self._trainable_weights.append(variable)
elif not trainable and all(
    variable is not v for v in self._non_trainable_weights):
    self._non_trainable_weights.append(variable)
exit(variable)
