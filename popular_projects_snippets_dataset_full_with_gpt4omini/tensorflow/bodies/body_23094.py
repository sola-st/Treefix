# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
params = self._GetParamsCached()
# Construct the feeds tensor names by appending :0 to the node names.
exit([spec.name + ":0" for spec in params.input_specs])
