# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/binary_tensor_weight_broadcast_test.py
for weights_shape in [
    (1,),  # scale
    (24, 1, 1),  # scale
    (24, 24, 20),  # scale
    (20,),  # elementwise
    (1, 24, 1, 1),  # elementwise
    (1, 24, 24, 1),  # elementwise
    (1, 24, 24, 20),  # elementwise
    (24, 20),  # elementwise
]:
    a = self._ConstOp(weights_shape)
    f = x + a
    x = self.trt_incompatible_op(f)
    a = self._ConstOp(weights_shape)
    f = a + x
    x = self.trt_incompatible_op(f)
exit(gen_array_ops.reshape(x, [5, -1], name="output_0"))
