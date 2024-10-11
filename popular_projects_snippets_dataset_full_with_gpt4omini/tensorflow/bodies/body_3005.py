# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_strided_slice_test.py
mlir_function = """
      func.func @test(%arg0: tensor<3xi32>) -> tensor<i32> {
        %cst_0 = "tf.Const"() {value = dense<1> : tensor<1xi32>}
                 : () -> tensor<1xi32>
        %cst_1 = "tf.Const"() {value = dense<0> : tensor<1xi32>}
                 : () -> tensor<1xi32>
        %0 = "tf.StridedSlice"(%arg0, %cst_1, %cst_0, %cst_0)
             {
               begin_mask       = 0 : i64,
               ellipsis_mask    = 0 : i64,
               end_mask         = 0 : i64,
               new_axis_mask    = 0 : i64,
               shrink_axis_mask = 1 : i64
             } : (tensor<3xi32>, tensor<1xi32>, tensor<1xi32>, tensor<1xi32>)
              -> tensor<i32>
        func.return %0 : tensor<i32>
      }"""

compiled = jitrt.compile(mlir_function, 'test')
arg0 = np.array([1, 2, 3], dtype=np.int32)
[res] = jitrt.execute(compiled, [arg0])
np.testing.assert_allclose(res, arg0[0], atol=0.0)
