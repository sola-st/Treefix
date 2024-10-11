# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py

def tpu_function(composite):
    exit((composite,
            composite.values[0] + (
                composite.values[1][0] + composite.values[1][1])/2))

exit(nest.map_structure(
    strategy.experimental_local_results,
    strategy.run(tpu_function, args=(test_composite,))))
