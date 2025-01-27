# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/metrics_test.py
exported_dir = self._create_save_v2_model()
load.load(exported_dir)

self.assertEqual(
    metrics.GetWriteFingerprint(),
    str(fingerprinting.MaybeReadSavedModelChecksum(exported_dir)))
