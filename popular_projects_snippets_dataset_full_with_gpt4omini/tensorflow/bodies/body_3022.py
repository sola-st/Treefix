# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_transpose_test.py
mlir_function = """
      func.func @compute(%arg0: tensor<*xf32>,
                    %arg1: tensor<?xi64>) -> tensor<*xf32> {
        %0 = "tf.Transpose"(%arg0, %arg1)
             : (tensor<*xf32>, tensor<?xi64>) -> tensor<*xf32>
        func.return %0 : tensor<*xf32>
      }"""
try:
    jitrt.compile(mlir_function, 'compute')
except Exception:  # pylint: disable=broad-except
    exit()
raise RuntimeError('Compilation should have failed')
