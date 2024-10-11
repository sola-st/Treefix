# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/metrics_test.py
read_v1_count = metrics.GetRead(write_version="1")
read_v2_count = metrics.GetRead(write_version="2")
load_v2_count = metrics.GetReadApi(load._LOAD_V2_LABEL)
load_v1_v2_count = metrics.GetReadApi(load_v1_in_v2._LOAD_V1_V2_LABEL)

save_dir = self._create_save_v1_model()
load.load(save_dir)

# Check that `load_v2` was *not* incremented.
self.assertEqual(metrics.GetReadApi(load._LOAD_V2_LABEL), load_v2_count)
self.assertEqual(metrics.GetRead(write_version="2"), read_v2_count)

self.assertEqual(
    metrics.GetReadApi(load_v1_in_v2._LOAD_V1_V2_LABEL),
    load_v1_v2_count + 1)
self.assertEqual(metrics.GetRead(write_version="1"), read_v1_count + 1)
