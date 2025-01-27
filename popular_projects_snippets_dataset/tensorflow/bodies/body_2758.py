# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/runtime/runner/testlib_runner_test.py
module = """
      func.func @returntensor(%arg0: memref<?xf32>) -> memref<4xf32> {
      %out = memref.alloc() : memref<4xf32>
      %c0 = arith.constant 0 : index
      %c1 = arith.constant 4 : index
      %step = arith.constant 1 : index

      scf.for %i = %c0 to %c1 step %step {
        %0 = memref.load %arg0[%i] : memref<?xf32>
        memref.store %0, %out[%i] : memref<4xf32>
      }

      return %out : memref<4xf32>
    }"""

arg = np.array([1.0, 2.0, 3.0, 4.0], dtype=np.float32)
[res] = r.execute(module, 'returntensor', [arg])

self.assertTrue(
    np.array_equal(res, np.array([1.0, 2.0, 3.0, 4.0], dtype=np.float32)))
