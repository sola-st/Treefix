# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/softmax_op_test.py
if test.is_gpu_available(cuda_only=True):
    rows = [2**x + np.random.randint(0, 16) for x in range(1, 4)]
    cols = [2**x + np.random.randint(0, 16) for x in range(1, 4)]
    for row, col in zip(rows, cols):
        logging.info("Testing softmax half dtype in shape [%d, %d]", row, col)
        data = np.random.rand(row, col)
        self._testAll(data.astype(np.float16))
