# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_monitors_test.py
mock_reader = test.mock.MagicMock()
monitor = debug_events_monitors.InfNanMonitor(mock_reader)
self.assertEmpty(monitor.alerts())
