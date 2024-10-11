# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
reader = io_ops.IdentityReader("test_reader")
produced = reader.num_records_produced()
queue = data_flow_ops.FIFOQueue(99, [dtypes.string], shapes=())
self.evaluate(queue.enqueue_many([["X", "Y", "Z"]]))
key, value = reader.read(queue)

self._ExpectRead(key, value, b"X")
self.assertAllEqual(1, self.evaluate(produced))
state = self.evaluate(reader.serialize_state())

self._ExpectRead(key, value, b"Y")
self._ExpectRead(key, value, b"Z")
self.assertAllEqual(3, self.evaluate(produced))

self.evaluate(queue.enqueue_many([["Y", "Z"]]))
self.evaluate(queue.close())
self.evaluate(reader.restore_state(state))
self.assertAllEqual(1, self.evaluate(produced))
self._ExpectRead(key, value, b"Y")
self._ExpectRead(key, value, b"Z")
with self.assertRaisesOpError("is closed and has insufficient elements "
                              "\\(requested 1, current size 0\\)"):
    self.evaluate([key, value])
self.assertAllEqual(3, self.evaluate(produced))

self.assertEqual(bytes, type(state))

with self.assertRaises(ValueError):
    reader.restore_state([])

with self.assertRaises(ValueError):
    reader.restore_state([state, state])

with self.assertRaisesOpError(
    "Could not parse state for IdentityReader 'test_reader'"):
    self.evaluate(reader.restore_state(state[1:]))

with self.assertRaisesOpError(
    "Could not parse state for IdentityReader 'test_reader'"):
    self.evaluate(reader.restore_state(state[:-1]))

with self.assertRaisesOpError(
    "Could not parse state for IdentityReader 'test_reader'"):
    self.evaluate(reader.restore_state(state + b"ExtraJunk"))

with self.assertRaisesOpError(
    "Could not parse state for IdentityReader 'test_reader'"):
    self.evaluate(reader.restore_state(b"PREFIX" + state))

with self.assertRaisesOpError(
    "Could not parse state for IdentityReader 'test_reader'"):
    self.evaluate(reader.restore_state(b"BOGUS" + state[5:]))
