# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/spacetobatch_op_test.py
x_np = [[[[1], [2], [3], [4]], [[5], [6], [7], [8]],
         [[9], [10], [11], [12]], [[13], [14], [15], [16]]],
        [[[17], [18], [19], [20]], [[21], [22], [23], [24]],
         [[25], [26], [27], [28]], [[29], [30], [31], [32]]]]
x_out = [[[[1], [3]], [[9], [11]]], [[[17], [19]], [[25], [27]]],
         [[[2], [4]], [[10], [12]]], [[[18], [20]], [[26], [28]]],
         [[[5], [7]], [[13], [15]]], [[[21], [23]], [[29], [31]]],
         [[[6], [8]], [[14], [16]]], [[[22], [24]], [[30], [32]]]]
block_size = 2
self._testOne(x_np, block_size, x_out)
