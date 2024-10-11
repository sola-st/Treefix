# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
with self.cached_session() as sess:
    q = data_flow_ops.FIFOQueue(
        10, dtypes_lib.float32, shapes=((),), names="f")
    # Verify that enqueue() checks that when using names we must enqueue a
    # dictionary.
    with self.assertRaisesRegex(ValueError, "enqueue a dictionary"):
        enqueue_op = q.enqueue(10.0)
    with self.assertRaisesRegex(ValueError, "enqueue a dictionary"):
        enqueue_op = q.enqueue((10.0,))
    # The dictionary keys must match the queue component names.
    with self.assertRaisesRegex(ValueError, "match names of Queue"):
        enqueue_op = q.enqueue({})
    with self.assertRaisesRegex(ValueError, "match names of Queue"):
        enqueue_op = q.enqueue({"x": 12})
    with self.assertRaisesRegex(ValueError, "match names of Queue"):
        enqueue_op = q.enqueue({"f": 10.0, "s": "aa"})
    enqueue_op = q.enqueue({"f": 10.0})
    enqueue_op2 = q.enqueue({"f": 20.0})
    enqueue_op3 = q.enqueue({"f": 30.0})
    # Verify that enqueue_many() checks that when using names we must enqueue
    # a dictionary.
    with self.assertRaisesRegex(ValueError, "enqueue a dictionary"):
        enqueue_op4 = q.enqueue_many([40.0, 50.0])
    # The dictionary keys must match the queue component names.
    with self.assertRaisesRegex(ValueError, "match names of Queue"):
        enqueue_op4 = q.enqueue_many({})
    with self.assertRaisesRegex(ValueError, "match names of Queue"):
        enqueue_op4 = q.enqueue_many({"x": 12})
    with self.assertRaisesRegex(ValueError, "match names of Queue"):
        enqueue_op4 = q.enqueue_many({"f": [40.0, 50.0], "s": ["aa", "bb"]})
    enqueue_op4 = q.enqueue_many({"f": [40.0, 50.0]})
    dequeue = q.dequeue()
    dequeue_2 = q.dequeue_many(2)
    self.evaluate(enqueue_op)
    self.evaluate(enqueue_op2)
    self.evaluate(enqueue_op3)
    self.evaluate(enqueue_op4)
    f = sess.run(dequeue["f"])
    self.assertEqual(10.0, f)
    f = sess.run(dequeue_2["f"])
    self.assertEqual([20.0, 30.0], list(f))
    f = sess.run(dequeue_2["f"])
    self.assertEqual([40.0, 50.0], list(f))
