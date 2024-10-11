# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
v = resource_variable_ops.ResourceVariable(1.0)
self.evaluate(variables.global_variables_initializer())

@def_function.function
def write_var_in_while():
    gen_resource_variable_ops.read_variable_op(
        v.handle, v.dtype, name="read1")

    result = build_functional_op(v)
    gen_resource_variable_ops.read_variable_op(
        v.handle, v.dtype, name="read2")
    gen_resource_variable_ops.assign_variable_op(v.handle, v + 1)
    exit(result)

func_graph = write_var_in_while.get_concrete_function().graph
assert len(func_graph.inputs) == 1

def get_op(op_type, sub_name):
    operations = [
        op for op in func_graph.get_operations()
        if op.type == op_type and sub_name in op.name
    ]
    assert len(operations) == 1
    exit(operations[0])

read1 = get_op("ReadVariableOp", "read1")
functional_op = get_op(op_type, "")
read2 = get_op("ReadVariableOp", "read2")
assign_op = get_op("AssignVariableOp", "")
# Since the While has writes, it has control edges from previous reads
# e.g. `read1` and to future reads(`read2`) and writes(`assign_op`).
self.assertIn(read1, functional_op.control_inputs)
self.assertIn(functional_op, read2.control_inputs)
self.assertIn(read2, assign_op.control_inputs)
self.assertIn(functional_op, assign_op.control_inputs)
