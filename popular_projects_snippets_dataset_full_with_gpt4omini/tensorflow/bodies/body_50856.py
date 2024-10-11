# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/metrics_test.py
write_count = metrics.GetWrite(write_version="2")
save_api_count = metrics.GetWriteApi(save._SAVE_V2_LABEL)
_ = self._create_save_v2_model()

self.assertEqual(
    metrics.GetWriteApi(save._SAVE_V2_LABEL), save_api_count + 1)
self.assertEqual(metrics.GetWrite(write_version="2"), write_count + 1)
