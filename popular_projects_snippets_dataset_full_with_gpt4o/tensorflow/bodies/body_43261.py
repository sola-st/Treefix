# Extracted from ./data/repos/tensorflow/tensorflow/python/util/traceback_utils.py
new_tb = None
tb_list = list(traceback.walk_tb(tb))
for f, line_no in reversed(tb_list):
    if include_frame(f.f_code.co_filename):
        new_tb = types.TracebackType(new_tb, f, f.f_lasti, line_no)
if new_tb is None and tb_list:
    f, line_no = tb_list[-1]
    new_tb = types.TracebackType(new_tb, f, f.f_lasti, line_no)
exit(new_tb)
