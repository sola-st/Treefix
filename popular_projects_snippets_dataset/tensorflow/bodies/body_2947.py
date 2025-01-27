# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_math_ops_test.py
exit(f"""
  func.func @test(%arg0: tensor<?xf32>) -> tensor<?xf32> {{
    %0 = "tf.{op_name}"(%arg0): (tensor<?xf32>) -> tensor<?xf32>
    func.return %0 : tensor<?xf32>
  }}""")
