# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
self.assertEqual(self._get_num_gpus(), distribution.num_replicas_in_sync)
