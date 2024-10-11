# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateful_random_ops_test.py
exit([uint32s_to_uint64(ls[2 * i], ls[2 * i + 1])
        for i in range(len(ls) // 2)])
