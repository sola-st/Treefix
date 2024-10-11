# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/analyzer_test.py
model_path = resource_loader.get_path_to_datafile('../testdata/add.bin')
mock_stdout = io.StringIO()
with test.mock.patch.object(sys, 'stdout', mock_stdout):
    analyzer.ModelAnalyzer.analyze(model_path=model_path)
txt = mock_stdout.getvalue()
self.assertIn('Subgraph#0(T#1) -> [T#2]', txt)
self.assertIn('Op#0 ADD(T#1, T#1) -> [T#0]', txt)
self.assertIn('Op#1 ADD(T#0, T#1) -> [T#2]', txt)
self.assertNotIn('Your model looks compatible with GPU delegate', txt)
