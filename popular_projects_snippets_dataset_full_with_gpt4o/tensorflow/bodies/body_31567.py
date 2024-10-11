# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_max_pool_op_test.py
"""Manual test by printing out intermediate result of a small random tensor.

    Since _GetExpectedFractionalMaxPoolResult is 'automated', it feel safer to
    have a test case that you can see what's happening.
    This test will generate a small, random, int 2D matrix, and feed it to
    FractionalMaxPool and _GetExpectedFractionalMaxPoolResult.
    """
num_rows = 6
num_cols = 6
tensor_shape = (1, num_rows, num_cols, 1)
pseudo_random = False
for overlapping in True, False:
    print("-" * 70)
    print("Testing FractionalMaxPool with overlapping = {}".format(
        overlapping))
    rand_mat = self._PRNG.randint(10, size=tensor_shape)
    pooling_ratio = [1, math.sqrt(2), math.sqrt(2), 1]
    with self.cached_session():
        p, r, c = nn_ops.fractional_max_pool_v2(
            rand_mat,
            pooling_ratio,
            pseudo_random,
            overlapping,
            seed=self._SEED)
        tensor_output, row_seq, col_seq = self.evaluate([p, r, c])
        expected_result = self._GetExpectedFractionalMaxPoolResult(rand_mat,
                                                                   row_seq,
                                                                   col_seq,
                                                                   overlapping)
        print("row sequence:")
        print(row_seq)
        print("column sequence:")
        print(col_seq)

        print("Input:")
        # Print input with pooling region marked.
        for i in range(num_rows):
            row_to_print = []
            for j in range(num_cols):
                if j in col_seq:
                    row_to_print.append("|")
                row_to_print.append(str(rand_mat[0, i, j, 0]))
            row_to_print.append("|")
            if i in row_seq:
                print("-" * 2 * len(row_to_print))
            print(" ".join(row_to_print))
        print("-" * 2 * len(row_to_print))

        print("Output from FractionalMaxPool:")
        print(tensor_output[0, :, :, 0])
        print("Expected result:")
        print(expected_result[0, :, :, 0])
