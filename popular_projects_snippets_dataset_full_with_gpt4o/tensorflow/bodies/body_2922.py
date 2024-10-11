# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen_test.py
mlir_code = tfr_gen(sys.modules[__name__], '_tfr_control_flow', [test_ops])
mlir_code_exp = r"""
      CHECK-LABEL: tfr.func @tf__test_two_inputs_op(%x: !tfr.tensor, %y: !tfr.tensor,
      CHECK-SAME:     %pred: i1{tfr.name="pred",tfr.default=false}) -> (!tfr.tensor) {
      CHECK-NEXT: %[[if:.*]] = scf.if %pred -> (!tfr.tensor) {
      CHECK-NEXT:   arith.constant true
      CHECK-NEXT:   scf.yield %x : !tfr.tensor
      CHECK-NEXT: } else {
      CHECK-NEXT:   arith.constant true
      CHECK-NEXT:   scf.yield %y : !tfr.tensor
      CHECK-NEXT:   }
      CHECK-NEXT:   tfr.return %if_stmt : !tfr.tensor
      CHECK-NEXT: }

      CHECK-LABEL: tfr.func @tf__test_three_inputs_op(%x: !tfr.tensor, %y: !tfr.tensor, %z: !tfr.tensor,
      CHECK-SAME:     %select: !tfr.attr{tfr.name="act",tfr.default="z"}) -> (!tfr.tensor) {
      CHECK-NEXT:   %[[cst:.*]] = tfr.constant "x" -> !tfr.attr
      CHECK-NEXT:   %[[eq:.*]] = tfr.equal %select, %[[cst]] -> i1
      CHECK-NEXT:   %[[if_stmt:.*]] = scf.if %[[eq]] -> (!tfr.tensor) {
      CHECK-NEXT:     %[[cst_1:.*]] = arith.constant true
      CHECK-NEXT:     scf.yield %x : !tfr.tensor
      CHECK-NEXT:   } else {
      CHECK-NEXT:     %[[cst_2:.*]] = tfr.constant "y" -> !tfr.attr
      CHECK-NEXT:     %[[eq_1:.*]] = tfr.equal %select, %[[cst_2]] -> i1
      CHECK-NEXT:     %[[if_stmt1:.*]] = scf.if %[[eq_1]] -> (!tfr.tensor) {
      CHECK-NEXT:       %[[cst_3:.*]] = arith.constant true
      CHECK-NEXT:       scf.yield %y : !tfr.tensor
      CHECK-NEXT:     } else {
      CHECK-NEXT:       %[[cst_4:.*]] = arith.constant true
      CHECK-NEXT:       scf.yield %z : !tfr.tensor
      CHECK-NEXT:     }
      CHECK-NEXT:     scf.yield %[[if_stmt1]] : !tfr.tensor
      CHECK-NEXT:   }
      CHECK-NEXT:   tfr.return %[[if_stmt]] : !tfr.tensor
      CHECK-NEXT: }

      CHECK-LABEL: tfr.func @tf__test_input_n_op(%x: !tfr.tensor_list) -> (!tfr.tensor) {
      CHECK-NEXT:   %[[n:.*]] = arith.constant 10 : i64
      CHECK-NEXT:   %[[cst:.*]] = arith.constant 0 : index
      CHECK-NEXT:   %[[elt:.*]] = tfr.get_element %x[%[[cst]]] : (!tfr.tensor_list, index) -> !tfr.tensor
      CHECK-NEXT:   %[[cst_1:.*]] = arith.constant 1 : i64
      CHECK-NEXT:   %[[begin:.*]] = arith.index_cast %[[cst_1]] : i64 to index
      CHECK-NEXT:   %[[end:.*]] = arith.index_cast %[[n]] : i64 to index
      CHECK-NEXT:   %[[step:.*]] = arith.constant 1 : index
      CHECK-NEXT:   %[[for_stmt:.*]] = scf.for %[[itr_1:.*]] = %[[begin]] to %[[end]] step %[[step]]
      CHECK-SAME:       iter_args(%[[it_arg:.*]] = %[[elt]]) -> (!tfr.tensor) {
      CHECK-NEXT:     %[[elt_1:.*]] = tfr.get_element %x[%itr_1] : (!tfr.tensor_list, index) -> !tfr.tensor
      CHECK-NEXT:     %[[Add:.*]] = tfr.call @tf__add(%[[it_arg]], %[[elt_1]]) : (!tfr.tensor, !tfr.tensor) -> (!tfr.tensor)
      CHECK-NEXT:     scf.yield %[[Add]] : !tfr.tensor
      CHECK-NEXT:   }
      CHECK-NEXT:   %{{.*}} = arith.constant true
      CHECK-NEXT:   tfr.return %[[for_stmt]] : !tfr.tensor
      CHECK-NEXT: }

      CHECK-LABEL: tfr.func @tf__test_input_n_op(%ins: !tfr.tensor_list) -> (!tfr.tensor) {
      CHECK: %[[attr:.*]] = tfr.constant i64 -> !tfr.attr
      CHECK: %Const = tfr.call @tf__const(%{{.*}}, %[[attr]]) : (!tfr.attr, !tfr.attr) -> (!tfr.tensor)
    """
self._check_code(mlir_code, mlir_code_exp)
