# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
results = []
iterator = iter(dataset)
# we iterate through the loop 5 times since we have 3 elements and a
# global batch of 2.
for _ in range(2):
    elem = next(iterator)
    output = distribution.experimental_local_results(
        distribution.run(step_fn, args=(elem,)))
    results.append(output)
exit(results)
