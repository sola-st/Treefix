# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
with self.cached_session() as sess:
    q = data_flow_ops.FIFOQueue(
        10, (dtypes_lib.float32, dtypes_lib.int32, dtypes_lib.string),
        shapes=((), (), ()),
        names=("f", "i", "s"))
    # Verify that enqueue() checks that when using names we must enqueue a
    # dictionary.
    with self.assertRaisesRegex(ValueError, "enqueue a dictionary"):
        enqueue_op = q.enqueue((10.0, 123, "aa"))
    # The dictionary keys must match the queue component names.
    with self.assertRaisesRegex(ValueError, "match names of Queue"):
        enqueue_op = q.enqueue({})
    with self.assertRaisesRegex(ValueError, "match names of Queue"):
        enqueue_op = q.enqueue({"x": 10.0})
    with self.assertRaisesRegex(ValueError, "match names of Queue"):
        enqueue_op = q.enqueue({"i": 12, "s": "aa"})
    with self.assertRaisesRegex(ValueError, "match names of Queue"):
        enqueue_op = q.enqueue({"i": 123, "s": "aa", "f": 10.0, "x": 10.0})
    enqueue_op = q.enqueue({"i": 123, "s": "aa", "f": 10.0})
    enqueue_op2 = q.enqueue({"i": 124, "s": "bb", "f": 20.0})
    enqueue_op3 = q.enqueue({"i": 125, "s": "cc", "f": 30.0})
    # Verify that enqueue_many() checks that when using names we must enqueue
    # a dictionary.
    with self.assertRaisesRegex(ValueError, "enqueue a dictionary"):
        enqueue_op4 = q.enqueue_many(([40.0, 50.0], [126, 127], ["dd", "ee"]))
    # The dictionary keys must match the queue component names.
    with self.assertRaisesRegex(ValueError, "match names of Queue"):
        enqueue_op4 = q.enqueue_many({})
    with self.assertRaisesRegex(ValueError, "match names of Queue"):
        enqueue_op4 = q.enqueue_many({"x": [10.0, 20.0]})
    with self.assertRaisesRegex(ValueError, "match names of Queue"):
        enqueue_op4 = q.enqueue_many({"i": [12, 12], "s": ["aa", "bb"]})
    with self.assertRaisesRegex(ValueError, "match names of Queue"):
        enqueue_op4 = q.enqueue_many({
            "f": [40.0, 50.0],
            "i": [126, 127],
            "s": ["dd", "ee"],
            "x": [1, 2]
        })
    enqueue_op4 = q.enqueue_many({
        "f": [40.0, 50.0],
        "i": [126, 127],
        "s": ["dd", "ee"]
    })
    dequeue = q.dequeue()
    dequeue_2 = q.dequeue_many(2)
    self.evaluate(enqueue_op)
    self.evaluate(enqueue_op2)
    self.evaluate(enqueue_op3)
    self.evaluate(enqueue_op4)
    i, f, s = sess.run([dequeue["i"], dequeue["f"], dequeue["s"]])
    self.assertEqual(123, i)
    self.assertEqual(10.0, f)
    self.assertEqual(compat.as_bytes("aa"), s)
    i, f, s = sess.run([dequeue_2["i"], dequeue_2["f"], dequeue_2["s"]])
    self.assertEqual([124, 125], list(i))
    self.assertTrue([20.0, 30.0], list(f))
    self.assertTrue([compat.as_bytes("bb"), compat.as_bytes("cc")], list(s))
    i, f, s = sess.run([dequeue_2["i"], dequeue_2["f"], dequeue_2["s"]])
    self.assertEqual([126, 127], list(i))
    self.assertTrue([40.0, 50.0], list(f))
    self.assertTrue([compat.as_bytes("dd"), compat.as_bytes("ee")], list(s))
