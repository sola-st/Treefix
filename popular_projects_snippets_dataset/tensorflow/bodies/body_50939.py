# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/pywrap_saved_model_metrics_test.py
self.assertEqual(
    self._get_histogram_proto(
        metrics.GetCheckpointReadDurations(api_label="bar")).num, 0)

metrics.AddCheckpointReadDuration(api_label="bar", microseconds=200)
metrics.AddCheckpointReadDuration(api_label="bar", microseconds=20000)

self.assertEqual(
    self._get_histogram_proto(
        metrics.GetCheckpointReadDurations(api_label="bar")).num, 2)
self.assertEqual(
    self._get_histogram_proto(
        metrics.GetCheckpointReadDurations(api_label="bar")).min, 200)
self.assertEqual(
    self._get_histogram_proto(
        metrics.GetCheckpointReadDurations(api_label="bar")).max, 20000)
