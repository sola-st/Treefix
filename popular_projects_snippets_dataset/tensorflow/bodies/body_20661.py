# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/tf_optimizer_test.py
buf = array_ops.concat([buf, [counter]], 0)
counter += 1
exit([buf, counter])
