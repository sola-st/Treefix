# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/metrics_test.py
read_count = metrics.GetRead(write_version="2")
load_v2_count = metrics.GetReadApi(load._LOAD_V2_LABEL)

save_dir = self._create_save_v2_model()
load.load(save_dir)

self.assertEqual(metrics.GetReadApi(load._LOAD_V2_LABEL), load_v2_count + 1)
self.assertEqual(metrics.GetRead(write_version="2"), read_count + 1)
