# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen_test.py
mlir_code = tfr_gen(sys.modules[__name__], '_tfr_attrs', [test_ops])
mlir_code_exp = r"""
      CHECK-LABEL: tfr.func @tf__test_num_attrs_op(
      CHECK-SAME:     %x: i64{tfr.name="x1",tfr.default=-10},
      CHECK-SAME:     %y: i64{tfr.name="y1",tfr.default=1},
      CHECK-SAME:     %x1: f32{tfr.name="x2",tfr.default=0.0},
      CHECK-SAME:     %y1: f32{tfr.name="y2",tfr.default=-3.0}) -> () {
      CHECK-NEXT: %{{.*}} = "tfr.build_list"(%x, %y) : (i64, i64) -> !tfr.attr
      CHECK-NEXT: %{{.*}} = arith.cmpi "eq", %x, %y : i64
      CHECK-NEXT: %{{.*}} = arith.cmpi "ult", %x, %y : i64
      CHECK-NEXT: %{{.*}} = arith.cmpi "ule", %x, %y : i64
      CHECK-NEXT: %{{.*}} = arith.cmpi "ugt", %x, %y : i64
      CHECK-NEXT: %{{.*}} = arith.cmpi "uge", %x, %y : i64
      CHECK-NEXT: %{{.*}} = arith.cmpi "ne", %x, %y : i64
      CHECK-NEXT: %{{.*}} = arith.addi %x, %y : i64
      CHECK-NEXT: %[[sub_1:.*]] = arith.subi %x, %y : i64
      CHECK-NEXT: %[[add_1:.*]] = arith.addi %[[sub_1]], %x : i64
      CHECK-NEXT: %[[cst:.*]] = arith.constant 1 : i64
      CHECK-NEXT: %{{.*}} = arith.addi %[[add_1]], %[[cst]] : i64
      CHECK-NEXT: %{{.*}} = arith.cmpf "ugt", %x1, %y1 : f32
      CHECK-NEXT: %{{.*}} = arith.addf %x1, %y1 : f32
      CHECK-NEXT: %{{.*}} = "tfr.build_list"(%x1, %y1) : (f32, f32) -> !tfr.attr
      CHECK-NEXT: %{{.*}} = arith.constant true
      CHECK-NEXT: tfr.return
      CHECK-NEXT: }

      CHECK-LABEL: tfr.func @tf__test_non_num_attrs_op(
      CHECK-SAME:     %x: !tfr.attr{tfr.name="z"},
      CHECK-SAME:     %y: !tfr.attr{tfr.name="x",tfr.default="hello"},
      CHECK-SAME:     %z: !tfr.attr{tfr.name="y",tfr.default=f32}) -> () {
      CHECK-NEXT: %{{.*}} = tfr.equal %x, %y -> i1
      CHECK-NEXT: %[[cst:.*]] = tfr.constant "test" -> !tfr.attr
      CHECK-NEXT: %{{.*}} = tfr.equal %x, %[[cst]] -> i1
      CHECK-NEXT: %{{.*}} = tfr.equal %y, %z -> i1
      CHECK-NEXT: %{{.*}} = arith.constant true
      CHECK-NEXT: tfr.return
      CHECK-NEXT: }
    """
self._check_code(mlir_code, mlir_code_exp)
