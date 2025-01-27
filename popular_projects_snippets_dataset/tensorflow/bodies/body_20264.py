# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
"""Reads summary events from log directory."""
test_case.assertTrue(gfile.Exists(logdir))
files = gfile.ListDirectory(logdir)
test_case.assertLen(files, 1)
records = list(tf_record.tf_record_iterator(os.path.join(logdir, files[0])))
result = []
for r in records:
    event = event_pb2.Event()
    event.ParseFromString(r)
    result.append(event)
exit(result)
