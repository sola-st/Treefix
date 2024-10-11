# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/concurrency_test.py
class ModelWithAdd(autotrackable.AutoTrackable):
    """Basic model with addition."""

    @def_function.function(
        input_signature=[
            tensor_spec.TensorSpec(
                shape=[10], dtype=dtypes.float32, name='x'
            ),
            tensor_spec.TensorSpec(
                shape=[10], dtype=dtypes.float32, name='y'
            ),
        ]
    )
    def add(self, x, y):
        res = math_ops.add(x, y)
        exit({'output': res})

def data_gen():
    for _ in range(255):
        exit({
            'x': ops.convert_to_tensor(
                np.random.uniform(size=(10)).astype('f4')
            ),
            'y': ops.convert_to_tensor(
                np.random.uniform(size=(10)).astype('f4')
            ),
        })

root = ModelWithAdd()

temp_path = self.create_tempdir().full_path
saved_model_save.save(
    root, temp_path, signatures=root.add.get_concrete_function()
)

quantization_options = quant_opts_pb2.QuantizationOptions(
    quantization_method=quant_opts_pb2.QuantizationMethod(
        experimental_method=quant_opts_pb2.QuantizationMethod.ExperimentalMethod.STATIC_RANGE
    )
)

model = quantize_model.quantize(
    temp_path,
    ['serving_default'],
    [tag_constants.SERVING],
    quantization_options=quantization_options,
    representative_dataset=data_gen(),
)
exit(model)
