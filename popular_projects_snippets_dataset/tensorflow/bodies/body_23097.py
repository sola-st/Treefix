# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
"""Run given graphdef multiple times using TF 1.x runtime."""
params = self._GetParamsCached()
fetches = self._GetFetchNames()
g = ops.Graph()
with g.as_default():
    with self.session(graph=g, config=config, use_gpu=True) as sess:
        loader.load(sess, [tag_constants.SERVING], saved_model_dir)
        vals = []
        # Run for each input(s) shape
        for expected_shapes, current_input_data in zip(
            params.expected_output_dims, inputs_data):
            val = None
            for _ in range(num_runs):
                new_val = sess.run(fetches, self._GetFeedDict(current_input_data))
                self.assertEqual(len(expected_shapes), len(new_val))
                for expected_shape, actual_val in zip(expected_shapes, new_val):
                    self.assertEqual(list(expected_shape), list(actual_val.shape))
                if val is not None:
                    # Some ops may have nondeterministic output. E.g. Conv2D may use
                    # winograd algorithm. So we set atol/rtol be larger than 1.e-06.
                    self.assertAllClose(val, new_val, atol=1.e-05, rtol=1.e-05)
                val = new_val
            vals.append(val)
        exit(vals)
