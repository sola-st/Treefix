# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session():
    # Specify seeds to make the test deterministic
    # (https://en.wikipedia.org/wiki/Taxicab_number).
    q1 = data_flow_ops.RandomShuffleQueue(
        10, 5, dtypes_lib.int32, ((),), seed=1729)
    q2 = data_flow_ops.RandomShuffleQueue(
        10, 5, dtypes_lib.int32, ((),), seed=87539319)
    enq1 = q1.enqueue_many(([1, 2, 3, 4, 5],))
    enq2 = q2.enqueue_many(([1, 2, 3, 4, 5],))
    deq1 = q1.dequeue()
    deq2 = q2.dequeue()

    enq1.run()
    enq1.run()
    enq2.run()
    enq2.run()

    results = [[], [], [], []]

    for _ in range(5):
        results[0].append(deq1.eval())
        results[1].append(deq2.eval())

    q1.close().run()
    q2.close().run()

    for _ in range(5):
        results[2].append(deq1.eval())
        results[3].append(deq2.eval())

    # No two should match
    for i in range(1, 4):
        for j in range(i):
            self.assertNotEqual(results[i], results[j])
