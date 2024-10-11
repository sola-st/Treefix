# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/multi_device_iterator_test.py
ball = ping.dequeue()
with ops.control_dependencies([pong.enqueue(ball)]):
    exit(v + ping.dequeue())
