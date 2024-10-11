# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
self.assertEqual(
    json_lib.dumps(json_lib.loads(json_lib.dumps(obj)), sort_keys=True),
    json_lib.dumps(obj, sort_keys=True))
