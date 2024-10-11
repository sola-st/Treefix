import traceback # pragma: no cover
class MockOperation: pass # pragma: no cover
def _compute_colocation_summary_from_op(op): return 'Colocation summary' # pragma: no cover
def _compute_device_assignment_summary_from_op(op): return 'Device assignment summary' # pragma: no cover
def create_mock_operation(): return MockOperation() # pragma: no cover

op = create_mock_operation() # pragma: no cover
traceback.format_list = lambda x: ['<traceback line>'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation.py
from l3.Runtime import _l_
r"""Return a dictionary mapping interpolation tokens to values.

  Args:
    op: op.Operation object.

  Returns:
    A dictionary mapping string tokens to string values.  The keys are shown
    below along with example values.
    {
      "file": "tool_utils.py",
      "lineno": "124",
      "line": "  source code line",
      "defined_at": " (defined at tool_utils.py:124)",
      "colocations":
          '''Node-device colocations active during op creation:
               with tf.compat.v1.colocate_with(test_node_1): <test_1.py:27>
               with tf.compat.v1.colocate_with(test_node_2): <test_2.py:38>'''
      "devices":
          '''Device assignments active during op 'foo' creation:
               with tf.device(/cpu:0): <test_1.py:27>
               with tf.device(some_func<foo.py, 123>): <test_2.py:38>'''
      "devs_and_colocs": A concatenation of colocations and devices, e.g.
          '''Node-device colocations active during op creation:
               with tf.compat.v1.colocate_with(test_node_1): <test_1.py:27>
               with tf.compat.v1.colocate_with(test_node_2): <test_2.py:38>'''
             Device assignments active during op 'foo' creation:
               with tf.device(/cpu:0): <test_1.py:27>
               with tf.device(some_func<foo.py, 123>): <test_2.py:38>'''
    }
  """
_l_(10083)
# TODO(xjun): colocation and device info are not displayed. Consider
# removing them or using vlog.
colocation_summary = _compute_colocation_summary_from_op(op)
_l_(10084)
device_summary = _compute_device_assignment_summary_from_op(op)
_l_(10085)
combined_summary = "\n".join([colocation_summary, device_summary])
_l_(10086)

if op.traceback is None:
    _l_(10098)

    # Some ops synthesized on as part of function or control flow definition
    # do not have tracebacks.
    filename = "<unknown>"
    _l_(10087)
    definition_traceback = ""
    _l_(10088)
    lineno = 0
    _l_(10089)
    line = ""
    _l_(10090)
    defined_at = "<unknown>"
    _l_(10091)
else:
    frame = op.traceback.last_user_frame()
    _l_(10092)
    filename = frame.filename
    _l_(10093)
    definition_traceback = traceback.format_list(op.traceback.get_user_frames())
    _l_(10094)
    lineno = frame.lineno
    _l_(10095)
    line = frame.line
    _l_(10096)
    defined_at = f"{filename}:{lineno:d}"
    _l_(10097)

field_dict = {
    "colocations": colocation_summary,
    "devices": device_summary,
    "devs_and_colocs": combined_summary,
    "defined_at": defined_at,
    "file": filename,
    "lineno": lineno,
    "line": line,
    "definition_traceback": definition_traceback,
}
_l_(10099)
aux = field_dict
_l_(10100)
exit(aux)
