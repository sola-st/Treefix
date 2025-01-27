# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/op_reg_gen_test.py
cxx_code = gen_register_op(sys.modules[__name__])
cxx_code_exp = r"""
      CHECK: #include "tensorflow/core/framework/op.h"
      CHECK-EMPTY
      CHECK: namespace tensorflow {
      CHECK-EMPTY
      CHECK-LABEL: REGISTER_OP("TestNoOp")
      CHECK-NEXT:      .Attr("T: numbertype")
      CHECK-NEXT:      .Output("o1: T");
      CHECK-EMPTY
      CHECK-LABEL: REGISTER_OP("TestCompositeOp")
      CHECK-NEXT:      .Input("x: T")
      CHECK-NEXT:      .Input("y: T")
      CHECK-NEXT:      .Attr("act: {'', 'relu'}")
      CHECK-NEXT:      .Attr("trans: bool = true")
      CHECK-NEXT:      .Attr("T: numbertype")
      CHECK-NEXT:      .Output("o1: T")
      CHECK-NEXT:      .Output("o2: T");
      CHECK-EMPTY
      CHECK:  }  // namespace tensorflow
    """
self.assertTrue(fw.check(str(cxx_code), cxx_code_exp), str(cxx_code))
