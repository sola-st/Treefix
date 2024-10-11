# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tensorflow/tests/tf_saved_model/dag_object_graph.py
super(TestModule, self).__init__()
self.child1 = Child()
self.child2 = self.child1
