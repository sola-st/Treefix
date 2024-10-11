# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/pywrap_saved_model_metrics_test.py
self.assertEqual(metrics.GetTrainingTimeSaved(api_label="baz"), 0)
metrics.AddTrainingTimeSaved(api_label="baz", microseconds=1000)
self.assertEqual(metrics.GetTrainingTimeSaved(api_label="baz"), 1000)
