# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/nullary_ops_test.py
with self.session() as session:
    with self.test_scope():
        output = op()
    result = session.run(output)
    self.assertAllClose(result, expected, rtol=1e-3)
