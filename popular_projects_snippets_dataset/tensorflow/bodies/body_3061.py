# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tensorflow/tests/tf_saved_model/cyclic_object_graph.py
super(ReferencesParent, self).__init__()
self.parent = parent
# CHECK: tf_saved_model.global_tensor
# CHECK-SAME: tf_saved_model.exported_names = ["child.my_variable"]
self.my_variable = tf.Variable(3.)
