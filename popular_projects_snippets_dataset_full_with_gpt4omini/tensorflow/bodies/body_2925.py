# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen_test.py
mlir_code = tfr_gen(sys.modules[__name__], '_tfr_shapes', [test_ops])
mlir_code_exp = r"""
      CHECK-LABEL: tfr.func @tf__test_identity_op(%x: !tfr.tensor) -> (!tfr.tensor) {
      CHECK-NEXT:   %[[shape:.*]] = tfr.get_shape %x -> !shape.shape

      CHECK-NEXT:   %[[shape_1:.*]] = tfr.get_shape %x -> !shape.shape
      CHECK-NEXT:   %[[len:.*]] = shape.rank %[[shape_1]] : !shape.shape -> !shape.size
      CHECK-NEXT:   %[[index:.*]] = shape.size_to_index %[[len]] : !shape.size
      CHECK-NEXT:   %[[begin:.*]] = arith.constant 0 : index
      CHECK-NEXT:   %[[step:.*]] = arith.constant 1 : index
      CHECK-NEXT:   scf.for %[[itr_1:.*]] = %[[begin]] to %[[index]] step %[[step]]  {
      CHECK-NEXT:     %[[size:.*]] = shape.get_extent %[[shape_1]], %[[itr_1]]: !shape.shape, index -> !shape.size
      CHECK-NEXT:     %[[elt:.*]] = shape.size_to_index %[[size]] : !shape.size
      CHECK-NEXT:     scf.yield
      CHECK-NEXT:   }

      CHECK-NEXT:   %[[cst:.*]] = arith.constant 1 : i64
      CHECK-NEXT:   %[[len_1:.*]] = shape.rank %shape_1 : !shape.shape -> !shape.size
      CHECK-NEXT:   %[[len_size_1:.*]] = shape.size_to_index %[[len_1]] : !shape.size
      CHECK-NEXT:   %[[cst_1:.*]] = arith.constant 2 : i64
      CHECK-NEXT:   %[[begin_1:.*]] = arith.index_cast %[[cst]] : i64 to index
      CHECK-NEXT:   %[[step_1:.*]] = arith.index_cast %[[cst_1]] : i64 to index
      CHECK-NEXT:   scf.for %[[itr_3:.*]] = %[[begin_1]] to %[[len_size_1]] step %[[step_1]]

      CHECK:        %[[cst:.*]] = tfr.constant i32 -> !tfr.attr
      CHECK-NEXT:   %[[Shape:.*]] = tfr.call @tf__shape(%x, %[[cst]]) : (!tfr.tensor, !tfr.attr) -> (!tfr.tensor)
      CHECK-NEXT:   %{{.*}} = arith.constant true
      CHECK-NEXT:   tfr.return %x : !tfr.tensor
      CHECK-NEXT: }
    """
self._check_code(mlir_code, mlir_code_exp)
