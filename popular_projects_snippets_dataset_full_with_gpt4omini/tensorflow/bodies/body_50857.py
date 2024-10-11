# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/metrics_test.py
write_count = metrics.GetWrite(write_version="1")
save_builder_count = metrics.GetWriteApi(builder_impl._SAVE_BUILDER_LABEL)
_ = self._create_save_v1_model()

self.assertEqual(
    metrics.GetWriteApi(builder_impl._SAVE_BUILDER_LABEL),
    save_builder_count + 1)
self.assertEqual(metrics.GetWrite(write_version="1"), write_count + 1)
