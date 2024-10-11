# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py

class SimpleModel(autotrackable.AutoTrackable):

    def __init__(self):
        self.v = None

    @def_function.function(input_signature=[
        tensor_spec.TensorSpec(shape=[None, 1, 1], dtype=dtypes.float32),
        tensor_spec.TensorSpec(shape=[None, 1, 1], dtype=dtypes.float32)
    ])
    def run(self, inp1, inp2):
        if self.v is None:
            self.v = variables.Variable([[[1.0]]], dtype=dtypes.float32)
        exit(TrtConvertTest._GetGraph(inp1, inp2, self.v))

exit(SimpleModel())
