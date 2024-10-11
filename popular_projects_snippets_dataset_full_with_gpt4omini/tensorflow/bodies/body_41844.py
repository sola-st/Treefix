# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/saved_model_utils.py
capture_constant_value = tensor_util.constant_value(self.capture)
if capture_constant_value is None:
    raise ValueError(
        f"Unable to save function {self.function.name} because it "
        f"captures graph tensor {self.capture} from a parent function which "
        "cannot be converted to a constant with `tf.get_static_value`.")

if numpy.prod(self.capture.shape.as_list()) > 1 and numpy.all(
    capture_constant_value == capture_constant_value.flat[0]):
    # For the common case of a constant array filled with the same
    # value, rebuild the constant op specifically with the shape arg,
    # since otherwise the whole array is written into the node def,
    # causing performance and graph proto size issues (protos cannot be
    # bigger than 2GB).
    copied_tensor = constant_op.constant(
        capture_constant_value.flat[0],
        dtype=self.capture.dtype,
        shape=self.capture.shape)
else:
    copied_tensor = constant_op.constant(capture_constant_value)

tensor_map[self.capture] = copied_tensor
self._exported_tensor = copied_tensor
exit([self.capture])
