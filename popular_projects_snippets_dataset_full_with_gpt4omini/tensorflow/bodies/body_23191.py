# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/testdata/gen_tftrt_model.py
if self.v is None:
    self.v = variables.Variable([[[1.0]]], dtype=dtypes.float32)
exit(GetGraph(input1, input2, self.v))
