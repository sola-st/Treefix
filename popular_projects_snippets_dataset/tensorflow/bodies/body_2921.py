# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen_test.py
mlir_code = tfr_gen(sys.modules[__name__], '_tfr_tensor', [test_ops])
mlir_code_exp = r"""
      CHECK-LABEL: tfr.func @tf__test_no_op() -> () {
      CHECK-NEXT:    tfr.return
      CHECK-NEXT: }

      CHECK-LABEL: tfr.func @tf__test_identity_op(%x: !tfr.tensor) -> (!tfr.tensor) {
      CHECK-NEXT: constant true
      CHECK-NEXT:    tfr.return %x : !tfr.tensor
      CHECK-NEXT: }

      CHECK-LABEL: tfr.func @tf__test_identity_n_op(%x: !tfr.tensor_list) -> (!tfr.tensor_list) {
      CHECK-NEXT: constant true
      CHECK-NEXT:    tfr.return %x : !tfr.tensor_list
      CHECK-NEXT: }

      CHECK-LABEL: tfr.func @tf__test_input_n_op(%x: !tfr.tensor_list) -> (!tfr.tensor) {
      CHECK-NEXT: constant true
      CHECK-NEXT: %[[index:.*]] = arith.constant 1 : index
      CHECK-NEXT: %[[sub:.*]] = tfr.get_element %x[%cst_1] : (!tfr.tensor_list, index) -> !tfr.tensor
      CHECK-NEXT: tfr.return %[[sub]] : !tfr.tensor
      CHECK-NEXT: }

      CHECK-LABEL: tfr.func @tf__test_output_n_op(%x: !tfr.tensor) -> (!tfr.tensor_list) {
      CHECK-NEXT: constant true
      CHECK-NEXT: %[[list:.*]] = "tfr.build_list"(%x, %x) : (!tfr.tensor, !tfr.tensor) -> !tfr.tensor_list
      CHECK-NEXT: tfr.return %[[list]] : !tfr.tensor_list
      CHECK-NEXT: }

      CHECK-LABEL: tfr.func @tf__test_two_inputs_op(%x: !tfr.tensor, %y: !tfr.tensor, %pred: i1{tfr.name="pred",tfr.default=false}) -> (!tfr.tensor) {
      CHECK-NEXT: %[[cst:.*]] = arith.constant 0 : i64
      CHECK-NEXT: %[[cst_1:.*]] = arith.constant 2 : i64
      CHECK-NEXT: %[[cst_2:.*]] = "tfr.constant_tensor"(%[[cst]]) : (i64) -> !tfr.tensor
      CHECK-NEXT: %[[Split:.*]] = tfr.call @tf__split(%[[cst_2]], %x, %[[cst_1]]) : (!tfr.tensor, !tfr.tensor, i64) -> (!tfr.tensor_list)
      CHECK-NEXT: %[[cst_4:.*]] = arith.constant 0 : index
      CHECK-NEXT: %[[elt:.*]] = tfr.get_element %[[Split]][%idx] : (!tfr.tensor_list, index) -> !tfr.tensor
      CHECK-NEXT: %[[cst_5:.*]] = arith.constant 1 : index
      CHECK-NEXT: %[[elt_1:.*]] = tfr.get_element %[[Split]][%idx_1] : (!tfr.tensor_list, index) -> !tfr.tensor
      CHECK-NEXT: constant true
      CHECK-NEXT: tfr.return %[[elt]] : !tfr.tensor
      CHECK-NEXT: }

      CHECK-LABEL: tfr.func @tf__test_two_outputs_op(%x: !tfr.tensor) -> (!tfr.tensor, !tfr.tensor) {
      CHECK-NEXT: %[[cst:.*]] = arith.constant 0 : i64
      CHECK-NEXT: %[[cst_1:.*]] = arith.constant 2 : i64
      CHECK-NEXT: %[[cst_2:.*]] = "tfr.constant_tensor"(%[[cst]]) : (i64) -> !tfr.tensor
      CHECK-NEXT: %[[Split:.*]] = tfr.call @tf__split(%[[cst_2]], %x, %[[cst_1]]) : (!tfr.tensor, !tfr.tensor, i64) -> (!tfr.tensor_list)
      CHECK-NEXT: constant true
      CHECK-NEXT: %[[cst_4:.*]] = arith.constant 0 : index
      CHECK-NEXT: %[[elt:.*]] = tfr.get_element %[[Split]][%cst_4] : (!tfr.tensor_list, index) -> !tfr.tensor
      CHECK-NEXT: %[[cst_5:.*]] = arith.constant 1 : index
      CHECK-NEXT: %[[elt_1:.*]] = tfr.get_element %[[Split]][%cst_5] : (!tfr.tensor_list, index) -> !tfr.tensor
      CHECK-NEXT: tfr.return %[[elt]], %[[elt_1]] : !tfr.tensor, !tfr.tensor
      CHECK-NEXT: }

      CHECK-LABEL: tfr.func @tf__test_num_attrs_op(%x1: i64{tfr.name="x1",tfr.default=-10}, %y1: i64{tfr.name="y1",tfr.default=1}, %x2: f32{tfr.name="x2",tfr.default=0.0}, %y2: f32{tfr.name="y2",tfr.default=-3.0}) -> () {
      CHECK-NEXT: %[[cst:.*]] = arith.constant 0 : i64
      CHECK-NEXT: %[[cst_1:.*]] = arith.constant 2 : i64
      CHECK-NEXT: %[[cst_2:.*]] = arith.constant 1 : i64
      CHECK-NEXT: %[[zero:.*]] = arith.constant 0 : i64
      CHECK-NEXT: %[[cst_3:.*]] = arith.subi %zero, %cst_2 : i64
      CHECK-NEXT: %[[list:.*]] = "tfr.build_list"(%[[cst]], %[[cst_1]], %[[cst_3]], %x1) : (i64, i64, i64, i64) -> !tfr.attr
      CHECK-NEXT: %[[cst_4:.*]] = arith.constant true
      CHECK-NEXT: %[[cst_5:.*]] = arith.constant false
      CHECK-NEXT: %[[cst_6:.*]] = "tfr.constant_tensor"(%[[list]]) : (!tfr.attr) -> !tfr.tensor
      CHECK-NEXT: %[[cst_7:.*]] = "tfr.constant_tensor"(%y1) : (i64) -> !tfr.tensor
      CHECK-NEXT: %[[cst_8:.*]] = "tfr.constant_tensor"(%[[cst_4]]) : (i1) -> !tfr.tensor
      CHECK-NEXT: %[[cst_9:.*]] = "tfr.constant_tensor"(%[[cst_5]]) : (i1) -> !tfr.tensor
      CHECK-NEXT: %[[cst_10:.*]] = arith.constant -1 : i64
      CHECK-NEXT: %[[OneHot:.*]] = tfr.call @tf__one_hot(%[[cst_6]], %[[cst_7]], %[[cst_8]], %[[cst_9]], %[[cst_10]])
      CHECK-SAME:   (!tfr.tensor, !tfr.tensor, !tfr.tensor, !tfr.tensor, i64) -> (!tfr.tensor)
      CHECK-NEXT: constant true
      CHECK-NEXT: tfr.return
      CHECK-NEXT: }
    """
self._check_code(mlir_code, mlir_code_exp)
