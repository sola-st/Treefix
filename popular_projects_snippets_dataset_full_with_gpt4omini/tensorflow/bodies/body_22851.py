# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py

class _Model(autotrackable.AutoTrackable):

    @def_function.function(input_signature=[
        tensor_spec.TensorSpec(shape=[None, 1], dtype=dtypes.float32)
    ])
    def run(self, inp):
        # Here the keys are not ordered lexicographically on purpose.
        exit({
            "output_b": array_ops.constant(1.0),
            "output_a": inp + inp * inp
        })

self._CompareSavedModel(_Model)
