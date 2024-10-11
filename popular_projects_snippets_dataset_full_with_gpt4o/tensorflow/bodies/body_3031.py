# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_controlflow_test.py
for specialize in specializations:
    mlir_function = """
        func.func @test(%arg0: tensor<i1>, %arg1: tensor<i1>, %arg2: tensor<?xf32>,
                   %arg3: tensor<?xf32>) -> tensor<?xf32> {
          %0 = "tf.IfRegion"(%arg0) ({
              %1 = "tf.If"(%arg1, %arg2, %arg3)
                 {then_branch = @add, else_branch = @sub, is_stateless = true}
                 : (tensor<i1>, tensor<?xf32>, tensor<?xf32>) -> tensor<?xf32>
              "tf.Yield"(%1) : (tensor<?xf32>) -> ()
            }, {
              %2 = "tf.Mul"(%arg2, %arg3) : (tensor<?xf32>, tensor<?xf32>)
                 -> tensor<?xf32>
              "tf.Yield"(%2) : (tensor<?xf32>) -> ()
            }) {is_stateless = false} : (tensor<i1>) -> tensor<?xf32>
          func.return %0: tensor<?xf32>
        }

        func.func @add(%arg0: tensor<?xf32>, %arg1: tensor<?xf32>) -> tensor<?xf32> {
          %0 = "tf.Add"(%arg0, %arg1): (tensor<?xf32>, tensor<?xf32>)
             -> tensor<?xf32>
          func.return %0 : tensor<?xf32>
        }

        func.func @sub(%arg0: tensor<?xf32>, %arg1: tensor<?xf32>) -> tensor<?xf32> {
          %0 = "tf.Sub"(%arg0, %arg1) : (tensor<?xf32>, tensor<?xf32>)
             -> tensor<?xf32>
          func.return %0 : tensor<?xf32>
        }"""
    compiled = jitrt.compile(mlir_function, 'test', specialize)

    d0 = np.random.randint(1, 100)

    arg0 = np.random.uniform(0.0, 10.0, size=(d0)).astype(np.float32)
    arg1 = np.random.uniform(0.0, 10.0, size=(d0)).astype(np.float32)

    true = np.array(True)
    false = np.array(False)
    [res] = jitrt.execute(compiled, [false, false, arg0, arg1])
    np.testing.assert_allclose(res, arg0 * arg1)
    [res] = jitrt.execute(compiled, [false, true, arg0, arg1])
    np.testing.assert_allclose(res, arg0 * arg1)
    [res] = jitrt.execute(compiled, [true, false, arg0, arg1])
    np.testing.assert_allclose(res, arg0 - arg1)
    [res] = jitrt.execute(compiled, [true, true, arg0, arg1])
    np.testing.assert_allclose(res, arg0 + arg1)
