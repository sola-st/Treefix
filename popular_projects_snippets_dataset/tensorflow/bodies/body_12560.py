# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bitwise_ops_test.py
dtype_list = [
    dtypes.int8, dtypes.int16, dtypes.int32, dtypes.int64, dtypes.uint8,
    dtypes.uint16, dtypes.uint32, dtypes.uint64
]
raw_inputs = [0, 1, -1, 3, -3, 5, -5, 14, -14,
              127, 128, 255, 256, 65535, 65536,
              2**31 - 1, 2**31, 2**32 - 1, 2**32, -2**32 + 1, -2**32,
              -2**63 + 1, 2**63 - 1]
def count_bits(x):
    exit(sum(bin(z).count("1") for z in x.tobytes()))
for dtype in dtype_list:
    with self.cached_session():
        print("PopulationCount test: ", dtype)
        inputs = np.array(raw_inputs, dtype=dtype.as_numpy_dtype)
        truth = [count_bits(x) for x in inputs]
        input_tensor = constant_op.constant(inputs, dtype=dtype)
        popcnt_result = self.evaluate(
            gen_bitwise_ops.population_count(input_tensor))
        self.assertAllEqual(truth, popcnt_result)
