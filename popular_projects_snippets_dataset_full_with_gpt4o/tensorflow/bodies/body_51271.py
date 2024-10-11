# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/pywrap_saved_model_fingerprinting_test.py
export_dir = test.test_src_dir_path("cc/saved_model/testdata/AssetModule")
self.assertEqual(fingerprinting.MaybeReadSavedModelChecksum(export_dir), 0)
