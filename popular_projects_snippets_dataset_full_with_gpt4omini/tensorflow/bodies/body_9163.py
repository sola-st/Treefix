# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer_test.py
with gfile.Open(outfile, 'r') as f:
    s = f.read()
    for attr in selected:
        self.assertTrue(s.find(attr) > 0, s)
    for attr in not_selected:
        self.assertFalse(s.find(attr) > 0, s)
