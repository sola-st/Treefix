# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen_test.py
mlir_code = tfr_gen(sys.modules[__name__], '_tfr_quant', [test_ops])
mlir_code_exp = r"""
      CHECK-LABEL: tfr.func @tf__test_identity_op(%x: !tfr.tensor) -> (!tfr.tensor) {
      CHECK-NEXT:   %[[raw_data:.*]] = tfr.quant_raw_data(%x) : (!tfr.tensor) -> (!tfr.tensor)
      CHECK-NEXT:   %[[qparam:.*]]:2 = tfr.quant_qparam(%x) : (!tfr.tensor) -> (!tfr.tensor, !tfr.tensor)
      CHECK:        %[[list:.*]] = "tfr.build_list"(%[[qparam]]#0, %[[qparam]]#0) : (!tfr.tensor, !tfr.tensor) -> !tfr.tensor_list
      CHECK:        %[[factor:.*]] = tfr.quant_scale_factor(%{{.*}}, %[[list]]) : (f32, !tfr.tensor_list) -> (!tfr.tensor)
      CHECK:        %[[list1:.*]] = "tfr.build_list"(%[[factor]]) : (!tfr.tensor) -> !tfr.tensor_list
      CHECK:        %[[factor1:.*]] = tfr.quant_scale_factor(%{{.*}}, %[[list1]]) : (f32, !tfr.tensor_list) -> (!tfr.tensor)
      CHECK-NEXT:   %[[Sub:.*]] = tfr.call @tf__sub(%[[raw_data]], %[[qparam]]#1) : (!tfr.tensor, !tfr.tensor) -> (!tfr.tensor)
      CHECK:        %[[act_range:.*]]:2 = tfr.quant_act_range(%{{.*}}, %{{.*}}, %{{.*}}) : (!tfr.attr, f32, i64) -> (!tfr.tensor, !tfr.tensor)
      CHECK:        %[[rescale:.*]] = tfr.quant_rescale(%[[Sub]], %[[factor1]], %{{.*}}) : (!tfr.tensor, !tfr.tensor, i64) -> (!tfr.tensor)
      CHECK:        %[[attr:.*]] = tfr.constant i16 -> !tfr.attr
      CHECK:        %[[Cast:.*]] = tfr.call @tf__cast(%[[rescale]], %[[attr]], %{{.*}}) : (!tfr.tensor, !tfr.attr, i1) -> (!tfr.tensor)
      CHECK:        %[[attr_1:.*]] = tfr.constant i8 -> !tfr.attr
      CHECK:        tfr.call @tf__cast(%[[Cast]], %[[attr_1]], %{{.*}}) : (!tfr.tensor, !tfr.attr, i1) -> (!tfr.tensor)
      CHECK:       }

      CHECK-LABEL: tfr.func @tf__test_identity_n_op(%x: !tfr.tensor_list) -> (!tfr.tensor_list) {
      CHECK-NEXT:   %[[raw_data:.*]] = tfr.quant_raw_data(%x) : (!tfr.tensor_list) -> (!tfr.tensor_list)
      CHECK:        tfr.return %[[raw_data:.*]] : !tfr.tensor_list
      CHECK:       }
    """
self._check_code(mlir_code, mlir_code_exp)
