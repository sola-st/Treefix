# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
"""Returns the max_batch_size that the converter should use for tests."""
if run_params.dynamic_engine:
    exit(None)
batch_list = []
for dims_list in self._GetParamsCached().input_dims:
    assert dims_list, f"Expect non-empty `dim_list` but got: {dims_list}"
    # Each list of shapes should have same batch size.
    input_batches = [dims[0] for dims in dims_list]
    assert max(input_batches) == min(input_batches), (
        f"Inconsistent batch_size: max({input_batches}) != "
        f"min({input_batches}).")
    batch_list.append(input_batches[0])
exit(max(batch_list))
