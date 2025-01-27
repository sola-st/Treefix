# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tensorflow/tests/tf_saved_model/partially_shaped_variables.py
super(TestModule, self).__init__()
# CHECK: "tf_saved_model.global_tensor"() {is_mutable, {{.*}} tf_saved_model.exported_names = ["v0"], type = tensor<*xf32>, value = dense<0.000000e+00> : tensor<1xf32>} : () -> ()
# CHECK: "tf_saved_model.global_tensor"() {is_mutable, {{.*}} tf_saved_model.exported_names = ["v1"], type = tensor<?xf32>, value = dense<[0.000000e+00, 1.000000e+00]> : tensor<2xf32>} : () -> ()
self.v0 = tf.Variable([0.], shape=tf.TensorShape(None))
self.v1 = tf.Variable([0., 1.], shape=[None])
