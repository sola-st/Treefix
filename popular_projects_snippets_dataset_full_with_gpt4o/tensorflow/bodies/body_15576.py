# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_squeeze_op_test.py
rt = ragged_factory_ops.constant([[[[[[[['H']], [['e']], [['l']], [['l']],
                                       [['o']]],
                                      [[['W']], [['o']], [['r']], [['l']],
                                       [['d']], [['!']]]]],
                                    [[[[['T']], [['h']], [['i']], [['s']]],
                                      [[['i']], [['s']]],
                                      [[['M']], [['e']], [['h']], [['r']],
                                       [['d']], [['a']], [['d']]],
                                      [[['.']]]]]]]])
output_list = [[['H', 'e', 'l', 'l', 'o'], ['W', 'o', 'r', 'l', 'd', '!']],
               [['T', 'h', 'i', 's'], ['i', 's'],
                ['M', 'e', 'h', 'r', 'd', 'a', 'd'], ['.']]]
ref = ragged_factory_ops.constant(output_list)
rt_s = ragged_squeeze_op.squeeze(rt, [0, 1, 3, 6, 7])
self.assertAllEqual(rt_s, ref)
