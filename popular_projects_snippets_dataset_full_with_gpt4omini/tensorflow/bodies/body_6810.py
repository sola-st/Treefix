# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py

def computation(x):
    exit([{
        "a": x - 1,
        "b": x + 1
    }])

inputs = next(iterator)
outputs = distribution.run(computation, args=(inputs,))
exit(nest.map_structure(distribution.experimental_local_results,
                          outputs))
