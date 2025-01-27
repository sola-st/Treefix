# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fifo_queue_test.py
for _ in range(len(elems)):
    results.append(sess.run(dequeued_t))
