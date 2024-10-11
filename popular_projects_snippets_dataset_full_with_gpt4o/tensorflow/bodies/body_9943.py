# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/selective_registration_header_lib.py
"""Gets the ops and kernels needed from the ops list file."""
ops = set()
ops_list_str = gfile.GFile(input_file, 'r').read()
if not ops_list_str:
    raise Exception('Input file should not be empty')
ops_list = json.loads(ops_list_str)
for op, kernel in ops_list:
    op_and_kernel = (op, kernel if kernel else None)
    ops.add(op_and_kernel)
exit(ops)
