# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
with self.assertRaisesRegex(ValueError, 'nvalid every_n_iter'):
    basic_session_run_hooks.LoggingTensorHook(tensors=['t'], every_n_iter=0)
with self.assertRaisesRegex(ValueError, 'nvalid every_n_iter'):
    basic_session_run_hooks.LoggingTensorHook(tensors=['t'], every_n_iter=-10)
with self.assertRaisesRegex(ValueError, 'xactly one of'):
    basic_session_run_hooks.LoggingTensorHook(
        tensors=['t'], every_n_iter=5, every_n_secs=5)
with self.assertRaisesRegex(ValueError, 'xactly one of'):
    basic_session_run_hooks.LoggingTensorHook(tensors=['t'])
