# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen_test.py
mlir_code = tfr_gen(sys.modules[__name__], '_tfr_loc', [test_ops])
mlir_code_exp = r"""
      CHECK-LABEL: tfr.func @tf__test_input_n_op(%x: !tfr.tensor_list) -> (!tfr.tensor) {
      CHECK-NEXT:   %[[n:.*]] = arith.constant 10 : i64
      CHECK-SAME        loc("tfr_gen_test.py":%{{.*}}:6)
      CHECK-NEXT:   %[[cst:.*]] = arith.constant 0 : index
      CHECK-SAME        loc("tfr_gen_test.py":%[[sum_line:.*]]:10)
      CHECK-NEXT:   %[[elt:.*]] = tfr.get_element %x[%[[cst]]] : (!tfr.tensor_list, index) -> !tfr.tensor
      CHECK-SAME        loc("tfr_gen_test.py":%[[sum_line]]:10)
      CHECK-NEXT:   %[[cst_1:.*]] = arith.constant 1 : i64
      CHECK-SAME        loc("tfr_gen_test.py":%[[for_line:.*]]:2)
      CHECK-NEXT:   %[[begin:.*]] = arith.index_cast %[[cst_1]] : i64 to index
      CHECK-SAME        loc("tfr_gen_test.py":%[[for_line]]:2)
      CHECK-NEXT:   %[[end:.*]] = arith.index_cast %[[n]] : i64 to index
      CHECK-SAME        loc("tfr_gen_test.py":%[[for_line]]:2)
      CHECK-NEXT:   %[[step:.*]] = arith.constant 1 : index
      CHECK-SAME        loc("tfr_gen_test.py":%[[for_line]]:2)
      CHECK-NEXT:   %[[for_stmt:.*]] = scf.for %[[itr_1:.*]] = %[[begin]] to %[[end]] step %[[step]]
      CHECK-SAME:       iter_args(%[[it_arg:.*]] = %[[elt]]) -> (!tfr.tensor) {
      CHECK-NEXT:     %[[elt_1:.*]] = tfr.get_element %x[%itr_1] : (!tfr.tensor_list, index) -> !tfr.tensor
      CHECK-SAME        loc("tfr_gen_test.py":%[[add_line:.*]]:34)
      CHECK-NEXT:     %[[Add:.*]] = tfr.call @tf__add(%[[it_arg]], %[[elt_1]]) : (!tfr.tensor, !tfr.tensor) -> (!tfr.tensor)
      CHECK-SAME        loc("tfr_gen_test.py":%[[add_line]]:12)
      CHECK-NEXT:     scf.yield %[[Add]] : !tfr.tensor
      CHECK-SAME        loc(unknown)
      CHECK-NEXT:   }
      CHECK-SAME        loc("tfr_gen_test.py":%[[for_line]]:2)
      CHECK-NEXT:   %{{.*}} = arith.constant true
      CHECK-SAME        loc(unknown)
      CHECK-NEXT:   tfr.return %[[for_stmt]] : !tfr.tensor
      CHECK-SAME        loc(unknown)
      CHECK-NEXT: }
      CHECK-SAME        loc("tfr_gen_test.py":%{{def_line:.*}}:0)
    """
self._check_code(mlir_code, mlir_code_exp)
