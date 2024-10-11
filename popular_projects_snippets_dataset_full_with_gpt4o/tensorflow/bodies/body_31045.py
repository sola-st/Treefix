# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
scale = 1.0507009873554804934193349852946
scale_alpha = 1.7580993408473768599402175208123
exit(np.where(np_features < 0, scale_alpha * (np.exp(np_features) - 1),
                scale * np_features))
