# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
"""Run given graphdef multiple times using TF 2.0 runtime."""
params = self._GetParamsCached()
root = load.load(saved_model_dir)
func = root.signatures[
    signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY]
results = []
for expected_shapes, current_input_data in zip(params.expected_output_dims,
                                               inputs_data):
    val = None
    for _ in range(num_runs):
        feed_dict = {
            params.input_specs[i].name: current_input_data[i]
            for i in range(len(params.input_specs))
        }
        new_val = func(**feed_dict)
        assert isinstance(
            new_val, dict), (f"Invalid type for `new_val`, expected `dict`. "
                             f"Got: {type(new_val)}.")
        # The key of the output map is always like output_i.
        new_val = [new_val[key] for key in sorted(new_val)]
        # Each element is an eager Tensor, and accessing individual elements is
        # very expensive, so we convert them to a numpy array first.
        new_val = [v.numpy() for v in new_val]
        self.assertEqual(len(expected_shapes), len(new_val))
        for expected_shape, actual_val in zip(expected_shapes, new_val):
            self.assertEqual(list(expected_shape), list(actual_val.shape))
        if val is not None:
            # Some ops may have nondeterministic output. E.g. Conv2D may use
            # winograd algorithm. So we set atol/rtol be larger than 1.e-06.
            self.assertAllClose(val, new_val, atol=1.e-05, rtol=1.e-05)
        val = new_val
    results.append(val)

exit(results)
