# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/pywrap_saved_model_metrics_test.py
self.assertEqual(
    self._get_histogram_proto(
        metrics.GetAsyncCheckpointWriteDurations(api_label="foo")).num, 0)

metrics.AddAsyncCheckpointWriteDuration(api_label="foo", microseconds=20)
metrics.AddAsyncCheckpointWriteDuration(api_label="foo", microseconds=50)

self.assertEqual(
    self._get_histogram_proto(
        metrics.GetAsyncCheckpointWriteDurations(api_label="foo")).num, 2)
self.assertEqual(
    self._get_histogram_proto(
        metrics.GetAsyncCheckpointWriteDurations(api_label="foo")).min, 20)
self.assertEqual(
    self._get_histogram_proto(
        metrics.GetAsyncCheckpointWriteDurations(api_label="foo")).max, 50)
