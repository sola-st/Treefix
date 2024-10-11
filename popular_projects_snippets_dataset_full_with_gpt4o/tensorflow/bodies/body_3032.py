# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_controlflow_test.py
for specialize in specializations:
    # Square input until one element is over 100.
    mlir_function = """
        func.func @test(%arg0: tensor<?x?xf32>) -> tensor<?x?xf32> {
          %0 = "tf.While"(%arg0)
             {body = @while_body, cond = @while_cond, is_stateless = true}
             : (tensor<?x?xf32>) -> (tensor<?x?xf32>)
          func.return %0: tensor<?x?xf32>
        }

        func.func @while_body(%arg0: tensor<?x?xf32>) -> tensor<?x?xf32> {
          %0 = "tf.Square"(%arg0): (tensor<?x?xf32>) -> tensor<?x?xf32>
          func.return %0: tensor<?x?xf32>
        }

        func.func @while_cond(%arg0: tensor<?x?xf32>) -> tensor<i1> {
          %cst = "tf.Const"() {value = dense<100.0> : tensor<f32>}
             : () -> tensor<f32>
          %less = "tf.Less"(%arg0, %cst) {T = f32}
             : (tensor<?x?xf32>, tensor<f32>) -> tensor<?x?xi1>
          %dim_to_reduce = "tf.Const"() {value = dense<[0, 1]> : tensor<2xi32>}
             : () -> tensor<2xi32>
          %all = "tf.All"(%less, %dim_to_reduce) {keep_dims = false}
             : (tensor<?x?xi1>, tensor<2xi32>) -> tensor<i1>
          func.return %all : tensor<i1>
        }"""
    compiled = jitrt.compile(mlir_function, 'test', specialize)

    d0 = np.random.randint(1, 100)
    d1 = np.random.randint(1, 100)

    arg0 = np.random.uniform(2.0, 10.0, size=(d0, d1)).astype(np.float32)

    np_res = arg0
    while np.all(np.less(np_res, 100)):
        np_res = np_res * np_res

    [res] = jitrt.execute(compiled, [arg0])
    np.testing.assert_allclose(res, np_res)
