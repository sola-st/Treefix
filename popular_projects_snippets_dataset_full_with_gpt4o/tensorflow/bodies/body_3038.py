# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_pack_test.py
self.pack_and_check(
    """
      func.func @test(%arg0: tensor<4xi32>, %arg1: tensor<4xi32>)
         -> tensor<2x4xi32> {
        %1 = "tf.Pack"(%arg0, %arg1) {axis = 0 : i64}
             : (tensor<4xi32>, tensor<4xi32>) -> tensor<2x4xi32>
        func.return %1 : tensor<2x4xi32>
      }""", (4), np.int32)
