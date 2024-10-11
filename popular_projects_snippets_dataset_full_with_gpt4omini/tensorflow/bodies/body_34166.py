# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/priority_queue_test.py
with self.cached_session():
    q = data_flow_ops.PriorityQueue(2000, (dtypes.string), (()))
    with self.assertRaises(TypeError):
        q.enqueue_many((["a", "b", "c"], ["a", "b", "c"])).run()
