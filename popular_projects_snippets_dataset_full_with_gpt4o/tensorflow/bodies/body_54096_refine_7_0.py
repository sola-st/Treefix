import traceback # pragma: no cover

def _compute_colocation_summary_from_op(op):# pragma: no cover
    return 'Node-device colocations active during op creation:\n    with tf.compat.v1.colocate_with(test_node_1): <test_1.py:27>\n    with tf.compat.v1.colocate_with(test_node_2): <test_2.py:38>' # pragma: no cover
def _compute_device_assignment_summary_from_op(op):# pragma: no cover
    return 'Device assignments active during op \'foo\' creation:\n    with tf.device(/cpu:0): <test_1.py:27>\n    with tf.device(some_func<foo.py, 123>): <test_2.py:38>' # pragma: no cover
op = type('MockOp', (object,), {# pragma: no cover
    'traceback': type('MockTraceback', (object,), {# pragma: no cover
        'last_user_frame': lambda: type('MockFrame', (object,), {# pragma: no cover
            'filename': 'tool_utils.py',# pragma: no cover
            'lineno': 124,# pragma: no cover
            'line': '  source code line'# pragma: no cover
        })(),# pragma: no cover
        'get_user_frames': lambda: [(None, 'test_file.py', 123, 'mocked_line'), (None, 'mocked_file.py', 456, 'mocked_line_2')]# pragma: no cover
    })()# pragma: no cover
})() # pragma: no cover

import traceback # pragma: no cover

def _compute_colocation_summary_from_op(op):# pragma: no cover
    return 'Node-device colocations active during op creation:\n    with tf.compat.v1.colocate_with(test_node_1): <test_1.py:27>\n    with tf.compat.v1.colocate_with(test_node_2): <test_2.py:38>' # pragma: no cover
def _compute_device_assignment_summary_from_op(op):# pragma: no cover
    return 'Device assignments active during op \u0027foo\u0027 creation:\n    with tf.device(/cpu:0): <test_1.py:27>\n    with tf.device(some_func<foo.py, 123>): <test_2.py:38>' # pragma: no cover
MockFrame = type('MockFrame', (object,), {# pragma: no cover
    'filename': 'tool_utils.py',# pragma: no cover
    'lineno': 124,# pragma: no cover
    'line': '  source code line'# pragma: no cover
}) # pragma: no cover
MockTraceback = type('MockTraceback', (object,), {# pragma: no cover
    'last_user_frame': lambda self: MockFrame,# pragma: no cover
    'get_user_frames': lambda self: [MockFrame]# pragma: no cover
}) # pragma: no cover
op = type('MockOp', (object,), {'traceback': MockTraceback()}) # pragma: no cover
traceback.format_list = lambda frames: ['(defined at tool_utils.py:124)'] # pragma: no cover

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
_l_(22377)
# TODO(xjun): colocation and device info are not displayed. Consider
# removing them or using vlog.
colocation_summary = _compute_colocation_summary_from_op(op)
_l_(22378)
device_summary = _compute_device_assignment_summary_from_op(op)
_l_(22379)
combined_summary = "\n".join([colocation_summary, device_summary])
_l_(22380)

if op.traceback is None:
    _l_(22392)

    # Some ops synthesized on as part of function or control flow definition
    # do not have tracebacks.
    filename = "<unknown>"
    _l_(22381)
    definition_traceback = ""
    _l_(22382)
    lineno = 0
    _l_(22383)
    line = ""
    _l_(22384)
    defined_at = "<unknown>"
    _l_(22385)
else:
    frame = op.traceback.last_user_frame()
    _l_(22386)
    filename = frame.filename
    _l_(22387)
    definition_traceback = traceback.format_list(op.traceback.get_user_frames())
    _l_(22388)
    lineno = frame.lineno
    _l_(22389)
    line = frame.line
    _l_(22390)
    defined_at = f"{filename}:{lineno:d}"
    _l_(22391)

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
_l_(22393)
aux = field_dict
_l_(22394)
exit(aux)
