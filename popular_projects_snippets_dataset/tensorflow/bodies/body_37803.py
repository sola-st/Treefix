# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
reader = io_ops.IdentityReader("test_reader")
work_completed = reader.num_work_units_completed()
produced = reader.num_records_produced()
queue = data_flow_ops.FIFOQueue(99, [dtypes.string], shapes=())
queued_length = queue.size()
key, value = reader.read(queue)

self.assertAllEqual(0, self.evaluate(work_completed))
self.assertAllEqual(0, self.evaluate(produced))
self.assertAllEqual(0, self.evaluate(queued_length))

self.evaluate(queue.enqueue_many([["A", "B", "C"]]))
self.evaluate(queue.close())
self.assertAllEqual(3, self.evaluate(queued_length))

self._ExpectRead(key, value, b"A")
self.assertAllEqual(1, self.evaluate(produced))

self._ExpectRead(key, value, b"B")

self._ExpectRead(key, value, b"C")
self.assertAllEqual(3, self.evaluate(produced))
self.assertAllEqual(0, self.evaluate(queued_length))

with self.assertRaisesOpError("is closed and has insufficient elements "
                              "\\(requested 1, current size 0\\)"):
    self.evaluate([key, value])

self.assertAllEqual(3, self.evaluate(work_completed))
self.assertAllEqual(3, self.evaluate(produced))
self.assertAllEqual(0, self.evaluate(queued_length))
