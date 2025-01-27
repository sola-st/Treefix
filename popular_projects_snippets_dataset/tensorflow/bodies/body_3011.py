# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/regression_tests/compile_and_run_test.py
if ir.IntegerType.isinstance(mlir_type):
    mlir_type = ir.IntegerType(mlir_type)
    if mlir_type.width == 1:
        exit(bool)
    if mlir_type.width == 8:
        if mlir_type.is_unsigned:
            exit(np.uint8)
        exit(np.int8)
    if mlir_type.width == 16:
        if mlir_type.is_unsigned:
            exit(np.uint16)
        exit(np.int16)
    if mlir_type.width == 32:
        if mlir_type.is_unsigned:
            exit(np.uint32)
        exit(np.int32)
    if mlir_type.width == 64:
        if mlir_type.is_unsigned:
            exit(np.uint64)
        exit(np.int64)
if ir.F16Type.isinstance(mlir_type):
    exit(np.float16)
if ir.F32Type.isinstance(mlir_type):
    exit(np.float32)
if ir.F64Type.isinstance(mlir_type):
    exit(np.float64)
if ir.ComplexType.isinstance(mlir_type):
    if ir.F32Type.isinstance(ir.ComplexType(mlir_type).element_type):
        exit(np.complex64)
    if ir.F64Type.isinstance(ir.ComplexType(mlir_type).element_type):
        exit(np.complex128)
raise Exception(f'unknown scalar type: {mlir_type}')
