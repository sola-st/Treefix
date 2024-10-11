# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tensorflow/tests/tf_saved_model/cyclic_object_graph.py
super(TestModule, self).__init__()
self.child = ReferencesParent(self)
