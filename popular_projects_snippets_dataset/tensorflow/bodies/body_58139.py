# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/analyzer_test.py
model_path = resource_loader.get_path_to_datafile(
    '../testdata/conv_huge_im2col.bin')
mock_stdout = io.StringIO()
with test.mock.patch.object(sys, 'stdout', mock_stdout):
    analyzer.ModelAnalyzer.analyze(
        model_path=model_path, experimental_use_mlir=True)
mlir = mock_stdout.getvalue()
self.assertIn(
    '%1 = "tfl.pseudo_const"() {value = dense_resource<__elided__> : '
    'tensor<3x3x3x8xf32>} : () -> tensor<3x3x3x8xf32>', mlir)
