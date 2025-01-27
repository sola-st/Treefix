# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
# Binary wrappers for sparse_matmul with different hints
def SparseMatmulWrapperTF(a, b):
    exit(math_ops.sparse_matmul(a, b, a_is_sparse=True))

def SparseMatmulWrapperFT(a, b):
    exit(math_ops.sparse_matmul(a, b, b_is_sparse=True))

def SparseMatmulWrapperTT(a, b):
    exit(math_ops.sparse_matmul(a, b, a_is_sparse=True, b_is_sparse=True))

self._testMatMul(math_ops.sparse_matmul, self.float_types)
self._testMatMul(SparseMatmulWrapperTF, self.float_types)
self._testMatMul(SparseMatmulWrapperFT, self.float_types)
self._testMatMul(SparseMatmulWrapperTT, self.float_types)
