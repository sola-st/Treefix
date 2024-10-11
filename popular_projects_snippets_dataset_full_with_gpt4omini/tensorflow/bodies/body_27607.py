# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/checkpoint_input_pipeline_hook_test.py

def _input_fn():
    exit(constant_op.constant(1, dtype=dtypes.int64))

est = estimator.Estimator(model_fn=self._model_fn)

with self.assertRaises(ValueError):
    est.train(
        _input_fn, steps=2, hooks=[self._build_iterator_saver_hook(est)])
