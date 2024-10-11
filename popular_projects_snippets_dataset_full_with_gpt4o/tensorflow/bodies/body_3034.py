# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_pack_test.py
self.pack_and_check(
    """
      func.func @test(%arg0: tensor<f32>, %arg1: tensor<f32>) -> tensor<2xf32> {
        %1 = "tf.Pack"(%arg0, %arg1) {axis = 0 : i64}
             : (tensor<f32>, tensor<f32>) -> tensor<2xf32>
        func.return %1 : tensor<2xf32>
      }""", (), np.float32)
