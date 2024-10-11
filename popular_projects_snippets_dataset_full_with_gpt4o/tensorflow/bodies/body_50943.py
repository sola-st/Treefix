# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/pywrap_saved_model_metrics_test.py
self.assertEqual(metrics.CalculateFileSize("not_a_file.txt"), -1)
