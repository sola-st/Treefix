# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
result = sess.run(
    "output:0",
    feed_dict={
        "input1:0": [[[1.0]]] * batch_size,
        "input2:0": [[[1.0]]] * batch_size
    })
self.assertAllEqual([[[5.0]]] * batch_size, result)
