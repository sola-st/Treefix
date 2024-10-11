# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/runtime/runner/testlib_runner_test.py
module = """
      func.func @addtensor(%arg0: memref<?xf32>) {
        %c0 = arith.constant 0 : index
        %c1 = arith.constant 3 : index
        %step = arith.constant 1 : index

        scf.for %i = %c0 to %c1 step %step {
          %0 = arith.constant 42.0 : f32
          %1 = memref.load %arg0[%i] : memref<?xf32>
          %2 = arith.addf %0, %1 : f32
          memref.store %2, %arg0[%i] : memref<?xf32>
        }
        
        func.return
      }"""

arg = np.array([1.0, 2.0, 3.0], dtype=np.float32)
[res] = r.execute(module, 'addtensor', [arg], inout=[0])
self.assertTrue(
    np.array_equal(res, np.array([43.0, 44.0, 45.0], dtype=np.float32)))
