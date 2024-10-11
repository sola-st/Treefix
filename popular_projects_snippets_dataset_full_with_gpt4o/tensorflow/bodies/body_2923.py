# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen_test.py
mlir_code = tfr_gen(sys.modules[__name__], '_tfr_tf_ops', [test_ops])
mlir_code_exp = r"""
      CHECK-LABEL: tfr.func @tf__test_complex_tf_op(%lhs: !tfr.tensor, %rhs: !tfr.tensor) -> (!tfr.tensor_list) {
      CHECK-NEXT:   %[[cst:.*]] = arith.constant 1 : i64
      CHECK-NEXT:   %[[zero:.*]] = arith.constant 0 : i64
      CHECK-NEXT:   %[[cst_1:.*]] = arith.subi %[[zero]], %cst : i64
      CHECK-NEXT:   %[[cst_2:.*]] = "tfr.constant_tensor"(%[[cst_1]]) : (i64) -> !tfr.tensor
      CHECK-NEXT:   %[[list:.*]] = "tfr.build_list"(%rhs, %[[cst_2]]) : (!tfr.tensor, !tfr.tensor) -> !tfr.tensor_list
      CHECK-NEXT:   %[[cst_3:.*]] = arith.constant 0 : i64
      CHECK-NEXT:   %[[cst_4:.*]] = arith.constant 2 : i64
      CHECK-NEXT:   %[[zero_1:.*]] = arith.constant 0 : i64
      CHECK-NEXT:   %[[pack:.*]] = tfr.call @tf__pack(%[[list]], %[[zero_1]]) : (!tfr.tensor_list, i64) -> !tfr.tensor
      CHECK-NEXT:   %[[cst_5:.*]] = "tfr.constant_tensor"(%[[cst_3]]) : (i64) -> !tfr.tensor
      CHECK-NEXT:   %[[SplitV:.*]] = tfr.call @tf__split_v(%lhs, %[[pack]], %[[cst_5]], %[[cst_4]])
      CHECK-NEXT:   %[[idx:.*]] = arith.constant 0 : index
      CHECK-NEXT:   %[[elt:.*]] = tfr.get_element %SplitV[%idx] : (!tfr.tensor_list, index) -> !tfr.tensor
      CHECK-NEXT:   %[[idx_1:.*]] = arith.constant 1 : index
      CHECK-NEXT:   %[[elt_1:.*]] = tfr.get_element %SplitV[%idx_1] : (!tfr.tensor_list, index) -> !tfr.tensor
      CHECK-NEXT:   %[[list_1:.*]] = "tfr.build_list"(%rhs, %rhs) : (!tfr.tensor, !tfr.tensor) -> !tfr.tensor_list
      CHECK-NEXT:   %[[cst_6:.*]] = arith.constant 1 : i64
      CHECK-NEXT:   %[[cst_7:.*]] = arith.constant 2 : i64
      CHECK-NEXT:   %[[zero_2:.*]] = arith.constant 0 : i64
      CHECK-NEXT:   %[[pack_1:.*]] = tfr.call @tf__pack(%[[list_1]], %[[zero_2]]) : (!tfr.tensor_list, i64) -> !tfr.tensor
      CHECK-NEXT:   %[[cst_8:.*]] = "tfr.constant_tensor"(%[[cst_6]]) : (i64) -> !tfr.tensor
      CHECK-NEXT:   %[[SplitV_1:.*]] = tfr.call @tf__split_v(%lhs, %[[pack_1]], %[[cst_8]], %[[cst_7]])
      CHECK-NEXT:   %[[idx_2:.*]] = arith.constant 0 : index
      CHECK-NEXT:   %[[elt_2:.*]] = tfr.get_element %SplitV_1[%idx_2] : (!tfr.tensor_list, index) -> !tfr.tensor
      CHECK-NEXT:   %[[idx_3:.*]] = arith.constant 1 : index
      CHECK-NEXT:   %[[elt_3:.*]] = tfr.get_element %SplitV_1[%idx_3] : (!tfr.tensor_list, index) -> !tfr.tensor
      CHECK-NEXT:   %[[cst_9:.*]] = arith.constant true
      CHECK-NEXT:   %[[list_2:.*]] = "tfr.build_list"(%[[elt]], %[[elt_3]]) : (!tfr.tensor, !tfr.tensor) -> !tfr.tensor_list
      CHECK-NEXT:   tfr.return %[[list_2]] : !tfr.tensor_list
      CHECK-NEXT:   }

      CHECK-LABEL: tfr.func @tf__test_identity_op(%x: !tfr.tensor) -> (!tfr.tensor) {
      CHECK-NEXT:    %cst = arith.constant true
      CHECK-NEXT:    %[[Id:.*]] = tfr.call @tf__identity(%x) : (!tfr.tensor) -> (!tfr.tensor)
      CHECK-NEXT:    tfr.return %[[Id]] : !tfr.tensor
      CHECK-NEXT: }

      CHECK-LABEL: tfr.func @tf__test_two_inputs_op(%x: !tfr.tensor, %y: !tfr.tensor,
      CHECK-SAME:     %pred: i1{tfr.name="pred",tfr.default=false}) -> (!tfr.tensor) {
      CHECK-NEXT:   %[[if_stmt:.*]] = scf.if %pred -> (!tfr.tensor) {
      CHECK-NEXT:     %cst = arith.constant true
      CHECK-NEXT:     %[[Add:.*]] = tfr.call @tf__add(%x, %y) : (!tfr.tensor, !tfr.tensor) -> (!tfr.tensor)
      CHECK-NEXT:     scf.yield %[[Add]] : !tfr.tensor
      CHECK-NEXT:   } else {
      CHECK-NEXT:     %cst_1 = arith.constant true
      CHECK-NEXT:     %[[cst_2:.*]] = arith.constant 0 : i64
      CHECK-NEXT:     %[[list:.*]] = "tfr.build_list"(%x, %y) : (!tfr.tensor, !tfr.tensor) -> !tfr.tensor_list
      CHECK-NEXT:     %[[Concat:.*]] = tfr.call @tf__concat(%[[cst_2]], %[[list]]) : (i64, !tfr.tensor_list) -> (!tfr.tensor)
      CHECK-NEXT:     scf.yield %[[Concat]] : !tfr.tensor
      CHECK-NEXT:   }
      CHECK-NEXT:   tfr.return %[[if_stmt]] : !tfr.tensor
      CHECK-NEXT: }

      CHECK-LABEL: tfr.func @tf__test_input_n_op(%ins: !tfr.tensor_list) -> (!tfr.tensor) {
      CHECK-NEXT:   %cst = arith.constant true
      CHECK-NEXT:   %[[cst_1:.*]] = arith.constant 0 : index
      CHECK-NEXT:   %[[elt:.*]] = tfr.get_element %ins[%cst_1] : (!tfr.tensor_list, index) -> !tfr.tensor
      CHECK-NEXT:   %[[cst_2:.*]] = arith.constant 1 : index
      CHECK-NEXT:   %[[elt_1:.*]] = tfr.get_element %ins[%cst_2] : (!tfr.tensor_list, index) -> !tfr.tensor
      CHECK-NEXT:   %[[cst_3:.*]] = arith.constant false
      CHECK-NEXT:   %[[call:.*]] = tfr.call @tf__test_two_inputs_op(
      CHECK-SAME:     %[[elt]], %[[elt_1]], %[[cst_3]]) : (!tfr.tensor, !tfr.tensor, i1) -> (!tfr.tensor)
      CHECK-NEXT:   tfr.return %[[call]] : !tfr.tensor
      CHECK-NEXT: }

      CHECK-LABEL: tfr.func @tf__add_(!tfr.tensor<T>,!tfr.tensor<T>) -> (!tfr.tensor<T>) attributes {T,f32_,i1_,i32_,i64_}

      CHECK-LABEL: tfr.func @tf__concat_(!tfr.tensor<i32_>,!tfr.tensor_list<N,T>) -> (!tfr.tensor<T>) attributes {N,T,f32_,i1_,i32_,i64_}

      CHECK-LABEL: tfr.func @tf__identity_(!tfr.tensor<T>) -> (!tfr.tensor<T>) attributes {T,f32_,i1_,i32_,i64_}

      CHECK-LABEL: tfr.func @tf__pack_(!tfr.tensor_list<N,T>,i64{tfr.name="axis",tfr.type="int"}) -> (!tfr.tensor<T>) attributes {N,T,axis,f32_,i1_,i32_,i64_}

      CHECK-LABEL: tfr.func @tf__split_v_(!tfr.tensor<T>,!tfr.tensor<Tlen>,!tfr.tensor<i32_>,i64{tfr.name="num_split",tfr.type="int"}) -> (!tfr.tensor_list<num_split,T>) attributes {T,Tlen,f32_,i1_,i32_,i64_,num_split}

      CHECK-LABEL: tfr.func @tf__test_complex_tf_op_(!tfr.tensor<T>,!tfr.tensor<Tlen>,i64{tfr.name="N",tfr.type="int"}) -> (!tfr.tensor_list<N,T>) attributes {N,T,Tlen,f32_,i1_,i32_,i64_}

      CHECK-LABEL: tfr.func @tf__test_identity_op_(!tfr.tensor<T>) -> (!tfr.tensor<T>) attributes {T,f32_,i1_,i32_,i64_}

      CHECK-LABEL: tfr.func @tf__test_input_n_op_(!tfr.tensor_list<N,T>) -> (!tfr.tensor<T>) attributes {N,T,f32_,i1_,i32_,i64_}

      CHECK-LABEL: tfr.func @tf__test_two_inputs_op_(!tfr.tensor<T>,!tfr.tensor<T>,i1{tfr.name="pred",tfr.type="bool"}) -> (!tfr.tensor<T>) attributes {T,f32_,i1_,i32_,i64_,pred}

      CHECK-LABEL: tfr.func @tf__test_two_outputs_op_(!tfr.tensor<T>) -> (!tfr.tensor<T>,!tfr.tensor<T>) attributes {T,f32_,i1_,i32_,i64_}
    """
self._check_code(mlir_code, mlir_code_exp)
