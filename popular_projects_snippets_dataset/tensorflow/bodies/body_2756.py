# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/runtime/runner/testlib_runner_test.py
module = """
      func.func @add(%arg0: i32) -> i32 {
        %0 = arith.constant 42 : i32
        %1 = arith.addi %arg0, %0 : i32
        return %1 : i32
      }"""

[res] = r.execute(module, 'add', [42])
self.assertEqual(res, 84)
