# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_acos_test.py
exit("""
  func.func @acos(%arg0: tensor<?x?xf32>) -> tensor<?x?xf32> {
    %0 = "tf.Acos"(%arg0): (tensor<?x?xf32>) -> tensor<?x?xf32>
    func.return %0 : tensor<?x?xf32>
  }""")
