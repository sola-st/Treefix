# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/checkpoint_input_pipeline_hook_test.py

def _input_fn():
    exit(dataset_ops.Dataset.range(10))

est = estimator.Estimator(model_fn=self._model_fn)

est.train(_input_fn, steps=2, hooks=[self._build_iterator_saver_hook(est)])
self.assertSequenceEqual(self._read_vars(est.model_dir), (2, 1))
est.train(_input_fn, steps=2, hooks=[self._build_iterator_saver_hook(est)])
self.assertSequenceEqual(self._read_vars(est.model_dir), (4, 3))
# Hook not provided, input pipeline was not restored.
est.train(_input_fn, steps=2)
self.assertSequenceEqual(self._read_vars(est.model_dir), (6, 1))
