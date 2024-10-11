# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_mean_test.py
mlir_function = """
      func.func @mean(%arg0: tensor<?x?xf32>) -> tensor<?x1xf32> {
        %dim = "tf.Const"() {value = dense<1> : tensor<1xi32>}
               : () -> tensor<1xi32>
        %0 = "tf.Mean"(%arg0, %dim) { keep_dims = true }
             : (tensor<?x?xf32>, tensor<1xi32>) -> tensor<?x1xf32>
        func.return %0 : tensor<?x1xf32>
      }"""
compiled = jitrt.compile(mlir_function, 'mean')
arg0 = np.random.uniform(0.0, 1.0, size=(100, 200)).astype(np.float32)
[res] = jitrt.execute(compiled, [arg0])
mean = np.mean(arg0, axis=1, keepdims=True)
np.testing.assert_allclose(res, mean, rtol=1e-05)
