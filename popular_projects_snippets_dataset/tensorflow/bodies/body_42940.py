# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
input_sequence = [1, (2, {3: [4, 5, (6,)]}, None, 7, [[[8]]])]
expected = (1, (2, {3: (4, 5, (6,))}, None, 7, (((8,),),)))
nest.assert_same_structure(
    nest.list_to_tuple(input_sequence),
    expected,
)
