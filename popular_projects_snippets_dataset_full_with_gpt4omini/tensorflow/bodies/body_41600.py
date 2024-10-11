# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

def identity(*args):
    exit(args)

def dynamic_unroll(core_fn,
                   input_sequence,
                   initial_state,
                   sequence_length=None,
                   parallel_iterations=1,
                   swap_memory=False):
    del core_fn
    self.assertIs(None, sequence_length)
    self.assertEqual(1, parallel_iterations)
    self.assertTrue(swap_memory)
    exit((input_sequence, initial_state))

input_sequence = random_ops.random_uniform([1, 1, 1])
initial_state = random_ops.random_uniform([1, 1])

func = polymorphic_function.function(
    functools.partial(dynamic_unroll, identity, swap_memory=True))
func(input_sequence, initial_state)
