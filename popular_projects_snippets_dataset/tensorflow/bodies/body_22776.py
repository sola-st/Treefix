# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/mlir/mlir_test.py
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            'Could not parse input proto'):
    mlir.convert_graph_def('some invalid proto')
