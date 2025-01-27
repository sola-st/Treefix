# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/jit/python_binding/tf_jitrt_test.py
exit("""
  func.func @log_1d(%arg0: tensor<?xf32>) -> tensor<?xf32> {
    %0 = "tf.Log"(%arg0): (tensor<?xf32>) -> tensor<?xf32>
    func.return %0 : tensor<?xf32>
  }""")
