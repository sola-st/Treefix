# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Initializes Operation from a TF_Operation."""

if not isinstance(g, Graph):
    raise TypeError(f"Operation initialization requires a Graph, "
                    f"got {type(g)} for argument g.")

if not isinstance(c_op, pywrap_tf_session.TF_Operation):
    raise TypeError(f"Operation initialization requires a TF_Operation, "
                    f"got {type(c_op)} for argument c_op.")

self._original_op = None

self._graph = g
self._c_op = c_op

# This will be set by self.inputs.
self._inputs_val = None

# List of _UserDevSpecs holding code location of device context manager
# invocations and the users original argument to them.
self._device_code_locations = None
# Dict mapping op name to file and line information for op colocation
# context managers.
self._colocation_code_locations = None
self._control_flow_context = g._get_control_flow_context()  # pylint: disable=protected-access

# Gradient function for this op. There are three ways to specify gradient
# function, and first available gradient gets used, in the following order.
# 1. self._gradient_function
# 2. Gradient name registered by "_gradient_op_type" attribute.
# 3. Gradient name registered by op.type.
self._gradient_function = None

op_def = g._get_op_def(pywrap_tf_session.TF_OperationOpType(c_op))  # pylint: disable=protected-access

self._is_stateful = op_def.is_stateful

# Initialize self._outputs.
num_outputs = pywrap_tf_session.TF_OperationNumOutputs(self._c_op)
self._outputs = []
for i in range(num_outputs):
    tf_output = c_api_util.tf_output(self._c_op, i)
    output_type = pywrap_tf_session.TF_OperationOutputType(tf_output)
    tensor = Tensor._create_with_tf_output(self, i, output_type, tf_output)  # pylint: disable=protected-access
    self._outputs.append(tensor)

self._id_value = g._add_op(self, self.name)  # pylint: disable=protected-access
