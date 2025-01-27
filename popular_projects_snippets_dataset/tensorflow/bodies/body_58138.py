# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/analyzer_test.py
model_path = resource_loader.get_path_to_datafile('../testdata/add.bin')
mock_stdout = io.StringIO()
with test.mock.patch.object(sys, 'stdout', mock_stdout):
    analyzer.ModelAnalyzer.analyze(
        model_path=model_path, experimental_use_mlir=True)
mlir = mock_stdout.getvalue()
self.assertIn(
    'func @main(%arg0: tensor<1x8x8x3xf32> '
    '{tf_saved_model.index_path = ["a"]}) -> '
    '(tensor<1x8x8x3xf32> {tf_saved_model.index_path = ["x"]}) attributes '
    '{tf.entry_function = {inputs = "input", outputs = "output"}, '
    'tf_saved_model.exported_names = ["serving_default"]}', mlir)
self.assertIn(
    '%0 = tfl.add %arg0, %arg0 {fused_activation_function = "NONE"} : '
    'tensor<1x8x8x3xf32>', mlir)
self.assertIn(
    '%1 = tfl.add %0, %arg0 {fused_activation_function = "NONE"} : '
    'tensor<1x8x8x3xf32>', mlir)
self.assertIn('return %1 : tensor<1x8x8x3xf32>', mlir)
