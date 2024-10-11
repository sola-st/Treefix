# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
reader = io_ops.IdentityReader("test_reader")
work_completed = reader.num_work_units_completed()
produced = reader.num_records_produced()
queue = data_flow_ops.FIFOQueue(99, [dtypes.string], shapes=())
queued_length = queue.size()
key, value = reader.read(queue)

self.evaluate(queue.enqueue_many([["X", "Y", "Z"]]))
self._ExpectRead(key, value, b"X")
self.assertLess(0, self.evaluate(queued_length))
self.assertAllEqual(1, self.evaluate(produced))

self._ExpectRead(key, value, b"Y")
self.assertLess(0, self.evaluate(work_completed))
self.assertAllEqual(2, self.evaluate(produced))

self.evaluate(reader.reset())
self.assertAllEqual(0, self.evaluate(work_completed))
self.assertAllEqual(0, self.evaluate(produced))
self.assertAllEqual(1, self.evaluate(queued_length))
self._ExpectRead(key, value, b"Z")

self.evaluate(queue.enqueue_many([["K", "L"]]))
self._ExpectRead(key, value, b"K")
