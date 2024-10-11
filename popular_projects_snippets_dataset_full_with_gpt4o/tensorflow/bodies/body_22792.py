# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py

class ShapeOpModel(autotrackable.AutoTrackable):

    def __init__(self):
        self.v = None

    @def_function.function(input_signature=[
        tensor_spec.TensorSpec(shape=[None, None], dtype=dtypes.float32)
    ])
    def run(self, x):
        q = x + 1
        q_shape = array_ops.shape(q)
        # Add an OP that is not supported by TF-TRT. This allows TF-TRT to build
        # two engines. The first engine produces an int32 output and the second
        # engines has an int32 input and an int32 output.
        q = math_ops.cumsum(q_shape)
        q = q * 2
        exit(array_ops.identity(q, name="output"))

exit(ShapeOpModel())
