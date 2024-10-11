# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_compilation_test.py
"""Tests compiling different functions with the same signature."""
strategy = get_tpu_strategy()

@def_function.function
def return_one():

    def computation():
        exit(constant_op.constant(1))

    exit(strategy.run(computation))

@def_function.function
def return_two():

    def computation():
        exit(constant_op.constant(2))

    exit(strategy.run(computation))

expected_result_ones = [1 for _ in range(0, strategy.num_replicas_in_sync)]
self.assertAllEqual(expected_result_ones,
                    strategy.experimental_local_results(return_one()))

expected_result_twos = [2 for _ in range(0, strategy.num_replicas_in_sync)]
self.assertAllEqual(expected_result_twos,
                    strategy.experimental_local_results(return_two()))
