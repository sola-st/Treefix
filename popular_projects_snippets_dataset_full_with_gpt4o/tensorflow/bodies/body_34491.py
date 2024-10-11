# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
"""Builds a graph that enqueues and dequeues a single float.

    Returns:
      A tuple with the graph init tensor and graph output tensor.
    """
q = data_flow_ops.FIFOQueue(1, "float")
init = q.enqueue(1.0)
x = q.dequeue()
q_inc = q.enqueue(x + 1)
exit((init, q_inc))
