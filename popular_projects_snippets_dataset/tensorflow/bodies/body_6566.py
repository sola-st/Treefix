# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py

def replica_step():
    with backprop.GradientTape() as tape:
        result = model()
    exit(tape.gradient(result, [model._v]))

exit(distribution.run(replica_step))
