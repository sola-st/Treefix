# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
exit(math_ops.reduce_sum(labels * math_ops.log(nn_ops.softmax(logits)),
                           1))
