# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/nullary_ops_test.py
with self.session():
    with self.test_scope():
        output = control_flow_ops.no_op()
    # This should not crash.
    output.run()
