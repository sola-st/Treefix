# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_logical_ops_test.py
exit(f"""
  func.func @test(%arg0: tensor<?xi1>, %arg1: tensor<?xi1>) -> tensor<?xi1> {{
    %0 = "tf.{op_name}"(%arg0, %arg1)
        : (tensor<?xi1>, tensor<?xi1>) -> tensor<?xi1>
    func.return %0 : tensor<?xi1>
  }}""")
