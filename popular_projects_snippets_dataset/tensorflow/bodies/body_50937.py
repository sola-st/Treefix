# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/pywrap_saved_model_metrics_test.py
self.assertEqual(
    self._get_histogram_proto(
        metrics.GetCheckpointWriteDurations(api_label="foo")).num, 0)

metrics.AddCheckpointWriteDuration(api_label="foo", microseconds=100)
metrics.AddCheckpointWriteDuration(api_label="foo", microseconds=200)

self.assertEqual(
    self._get_histogram_proto(
        metrics.GetCheckpointWriteDurations(api_label="foo")).num, 2)
self.assertEqual(
    self._get_histogram_proto(
        metrics.GetCheckpointWriteDurations(api_label="foo")).min, 100)
self.assertEqual(
    self._get_histogram_proto(
        metrics.GetCheckpointWriteDurations(api_label="foo")).max, 200)
