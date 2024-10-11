# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_matmul_test.py
exit("""
  func.func @matmul(%arg0: tensor<?x?xf32>,
               %arg1: tensor<?x?xf32>) -> tensor<?x?xf32> {
    %0 = "tf.MatMul"(%arg0, %arg1) {
           transpose_a = false,
           transpose_b = false
         } : (tensor<?x?xf32>, tensor<?x?xf32>) -> tensor<?x?xf32>
    func.return %0 : tensor<?x?xf32>
  }""")
