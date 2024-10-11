# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_log1p_test.py
exit("""
  func.func @log1p(%arg0: tensor<?x?xf32>) -> tensor<?x?xf32> {
    %0 = "tf.Log1p"(%arg0): (tensor<?x?xf32>) -> tensor<?x?xf32>
    func.return %0 : tensor<?x?xf32>
  }""")
