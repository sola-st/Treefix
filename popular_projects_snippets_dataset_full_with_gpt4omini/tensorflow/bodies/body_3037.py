# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_pack_test.py
self.pack_and_check(
    """
      func.func @test(%arg0: tensor<i1>, %arg1: tensor<i1>) -> tensor<2xi1> {
        %1 = "tf.Pack"(%arg0, %arg1) {axis = 0 : i64}
             : (tensor<i1>, tensor<i1>) -> tensor<2xi1>
        func.return %1 : tensor<2xi1>
      }""", (), bool)
