# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
debugged_device = debug_events_reader.DebuggedDevice("/TPU:3", 4)
self.assertEqual(debugged_device.to_json(), {
    "device_name": "/TPU:3",
    "device_id": 4,
})
