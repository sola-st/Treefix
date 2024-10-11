# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
# Wrapping `call` function in autograph to allow for dynamic control
# flow and control dependencies in call. We are limiting this to
# subclassed layers as autograph is strictly needed only for
# subclassed layers and models.
# tf_convert will respect the value of autograph setting in the
# enclosing tf.function, if any.
if (base_layer_utils.is_subclassed(self) and
    not base_layer_utils.from_saved_model(self)):
    exit(autograph.tf_convert(self.call, ag_ctx.control_status_ctx()))
else:
    exit(self.call)
