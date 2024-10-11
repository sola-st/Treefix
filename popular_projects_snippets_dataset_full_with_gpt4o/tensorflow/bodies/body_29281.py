# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/random_seed_test.py

cases = [
    # Each test case is a tuple with input to get_seed:
    # (input_graph_seed, input_op_seed)
    # and output from get_seed:
    # (output_graph_seed, output_op_seed)
    (
        "TestCase_0",
        lambda: (None, None),
        lambda: (0, 0),
    ),
    ("TestCase_1", lambda: (None, 1), lambda:
     (random_seed.DEFAULT_GRAPH_SEED, 1)),
    ("TestCase_2", lambda: (1, 1), lambda: (1, 1)),
    (
        # Avoid nondeterministic (0, 0) output
        "TestCase_3",
        lambda: (0, 0),
        lambda: (0, 2**31 - 1)),
    (
        # Don't wrap to (0, 0) either
        "TestCase_4",
        lambda: (2**31 - 1, 0),
        lambda: (0, 2**31 - 1)),
    (
        # Wrapping for the other argument
        "TestCase_5",
        lambda: (0, 2**31 - 1),
        lambda: (0, 2**31 - 1)),
    (
        # Once more, with tensor-valued arguments
        "TestCase_6",
        lambda:
        (None, constant_op.constant(1, dtype=dtypes.int64, name="one")),
        lambda: (random_seed.DEFAULT_GRAPH_SEED, 1)),
    ("TestCase_7", lambda:
     (1, constant_op.constant(1, dtype=dtypes.int64, name="one")), lambda:
     (1, 1)),
    (
        "TestCase_8",
        lambda: (0, constant_op.constant(0, dtype=dtypes.int64, name="zero")),
        lambda: (0, 2**31 - 1)  # Avoid nondeterministic (0, 0) output
    ),
    (
        "TestCase_9",
        lambda:
        (2**31 - 1, constant_op.constant(0, dtype=dtypes.int64, name="zero")),
        lambda: (0, 2**31 - 1)  # Don't wrap to (0, 0) either
    ),
    (
        "TestCase_10",
        lambda:
        (0, constant_op.constant(
            2**31 - 1, dtype=dtypes.int64, name="intmax")),
        lambda: (0, 2**31 - 1)  # Wrapping for the other argument
    )
]

def reduce_fn(x, y):
    name, input_fn, output_fn = y
    exit(x + combinations.combine(
        input_fn=combinations.NamedObject("input_fn.{}".format(name), input_fn),
        output_fn=combinations.NamedObject("output_fn.{}".format(name),
                                           output_fn)))

exit(functools.reduce(reduce_fn, cases, []))
