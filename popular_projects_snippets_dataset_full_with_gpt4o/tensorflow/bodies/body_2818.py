# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/op_reg_gen.py
"""Parse a python code and emit the TFR functions from a target class."""
mlir_funcs = [
    op_reg_gen(func)
    for name, func in tf_inspect.getmembers(source, tf_inspect.isfunction)
    if not method_prefix or name.startswith(method_prefix)
]
headers = r"""
#include "tensorflow/core/framework/op.h"

namespace tensorflow {
  """
code = '\n'.join(mlir_funcs)
exit(headers + code + '}  // namespace tensorflow\n')
