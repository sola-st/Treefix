# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
if not test.is_gpu_available(cuda_only=True):
    self.skipTest('GPU required')

checkpoint_path = self.get_temp_dir()
self._train(checkpoint_path)
vars_expected = self._train(checkpoint_path, restore=True)
vars_layout_optimized = self._train(
    checkpoint_path, restore=True, layout_optimizer=True)

for var_expected, var_layout_optimized in zip(vars_expected,
                                              vars_layout_optimized):
    self.assertAllClose(var_expected, var_layout_optimized, atol=1e-6)
