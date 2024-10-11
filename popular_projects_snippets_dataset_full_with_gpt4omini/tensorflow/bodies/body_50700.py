# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer_test.py
with self.assertRaises(TypeError):
    test_dir = self._CleanTestDir("basics_string_instead_of_graph")
    sw = self._FileWriter(test_dir, "string instead of graph object")
    sw.close()
