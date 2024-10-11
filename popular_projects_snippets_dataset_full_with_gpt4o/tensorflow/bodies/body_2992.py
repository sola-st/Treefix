# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_binary_bcast_test.py
mlir_function = """
      func.func @compute(%arg0: tensor<*xf32>,
                    %arg1: tensor<f32> {rt.constraint = "value"})
          -> tensor<*xf32> {
        %0 = "tf.AddV2"(%arg0, %arg1)
             : (tensor<*xf32>, tensor<f32>) -> tensor<*xf32>
        func.return %0 : tensor<*xf32>
      }"""

with self.assertRaisesRegex(Exception,
                            'cannot sink operand type: tensor<f32>'):
    jitrt.compile(mlir_function, 'compute')
