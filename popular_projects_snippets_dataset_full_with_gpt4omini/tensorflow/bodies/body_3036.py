# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_pack_test.py
self.pack_and_check(
    """
      func.func @test(%arg0: tensor<i64>, %arg1: tensor<i64>) -> tensor<2xi64> {
        %1 = "tf.Pack"(%arg0, %arg1) {axis = 0 : i64}
             : (tensor<i64>, tensor<i64>) -> tensor<2xi64>
        func.return %1 : tensor<2xi64>
      }""", (), np.int64)
