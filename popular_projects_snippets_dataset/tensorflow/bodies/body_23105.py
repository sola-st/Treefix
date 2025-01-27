# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
for shapes in self._GetParamsCached().input_dims:
    exit([
        array_ops.zeros(x, dtype=spec.dtype)
        for (x, spec) in zip(shapes,
                             self._GetParamsCached().input_specs)
    ])
