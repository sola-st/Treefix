# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_binary_bcast_test.py
mlir_function = """
      func.func @compute(%arg0: tensor<?xf32>, %arg1: tensor<?xf32>)
          -> tensor<?xf32> {
        %0 = "tf.AddV2"(%arg0, %arg1)
             : (tensor<?xf32>, tensor<?xf32>) -> tensor<?xf32>
        func.return %0 : tensor<?xf32>
      }"""

arg0 = np.random.uniform(0, 10.0, size=(2)).astype(np.float32)
arg1 = np.random.uniform(0, 10.0, size=(3)).astype(np.float32)

for specialize in specializations:
    compiled = jitrt.compile(mlir_function, 'compute', specialize)

    with self.assertRaisesRegex(Exception, 'required broadcastable shapes'):
        jitrt.execute(compiled, [arg0, arg1])
