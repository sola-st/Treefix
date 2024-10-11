# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
if (test_util.IsMklEnabled() and
    _get_graph_matmul_dtype() in _mkl_matmul_supported_types()):
    exit("_MklMatMul")
else:
    exit("MatMul")
