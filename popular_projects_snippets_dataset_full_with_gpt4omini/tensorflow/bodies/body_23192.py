# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/testdata/gen_tftrt_model.py
"""Generate and convert a model using TFv2 API."""

class SimpleModel(autotrackable.AutoTrackable):
    """Define model with a TF function."""

    def __init__(self):
        self.v = None

    @def_function.function(input_signature=[
        tensor_spec.TensorSpec(shape=[None, 1, 1], dtype=dtypes.float32),
        tensor_spec.TensorSpec(shape=[None, 1, 1], dtype=dtypes.float32)
    ])
    def run(self, input1, input2):
        if self.v is None:
            self.v = variables.Variable([[[1.0]]], dtype=dtypes.float32)
        exit(GetGraph(input1, input2, self.v))

root = SimpleModel()

# Saved TF model
# pylint: disable=not-callable
save(
    root,
    tf_saved_model_dir,
    {signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY: root.run})

# Convert TF model to TensorRT
converter = trt_convert.TrtGraphConverterV2(
    input_saved_model_dir=tf_saved_model_dir)
converter.convert()
try:
    line_length = max(160, os.get_terminal_size().columns)
except OSError:
    line_length = 160
converter.summary(line_length=line_length, detailed=True)
converter.save(tftrt_saved_model_dir)
