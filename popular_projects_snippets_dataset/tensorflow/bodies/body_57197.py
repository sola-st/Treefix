# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/is_finite.py
result = []
for dim in shape:
    result.append(np.random.randint(low=0, high=dim))
exit(tuple(result))
