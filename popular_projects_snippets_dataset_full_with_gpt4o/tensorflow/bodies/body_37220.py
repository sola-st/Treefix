# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session() as sess:
    v1 = variables.VariableV1([0.0])
    v2 = variables.VariableV1([1.0])

    # Group init1 and init2 and run.
    init = control_flow_ops.group(v1.initializer, v2.initializer)
    # Fetching v1 directly will result in an uninitialized error
    with self.assertRaisesOpError("Attempting to use uninitialized value"):
        self.evaluate(v1)

    # Runs "init" before fetching v1 and v2.
    init.run()
    v1_val, v2_val = self.evaluate([v1, v2])

# Ensure that v1 and v2 are initialized
self.assertAllClose([0.0], v1_val)
self.assertAllClose([1.0], v2_val)
