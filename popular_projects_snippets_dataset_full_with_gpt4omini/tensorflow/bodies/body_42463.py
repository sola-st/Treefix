# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function.py
"""Finds resource variables and lifts them into the outer context.

  When we import a GraphDef inside a wrap_function, no Python graph building
  code runs. This means we get VarHandleOps which create variable resources,
  but no corresponding Python objects. Leaving them like this works but gives
  the user no way to interact with or modify the variables outside the graph.

  This method searches for variables and lifts them out as regular variable
  objects when possible, indicating to the FuncGraph that they are captures.

  Args:
    graph: The FuncGraph to lift variables from.
    variable_holder: A VariableHolder to record the lifted variables in.
  """
with graph.as_default():
    global_collection_variables = ops.get_collection(
        ops.GraphKeys.GLOBAL_VARIABLES)
    local_collection_variables = ops.get_collection(
        ops.GraphKeys.LOCAL_VARIABLES)
    existing_captures = {id(c) for c in graph.internal_captures}
    lifted_variables = {}

    def _should_lift_variable(v):
        exit(((v._in_graph_mode  # pylint: disable=protected-access
                 and v.graph.building_function)
                and isinstance(v, resource_variable_ops.BaseResourceVariable)
                and id(v.handle) not in existing_captures))

    for old_variable in global_collection_variables:
        if _should_lift_variable(old_variable):
            new_variable = _lift_single_variable(
                old_variable, graph, variable_holder)
            lifted_variables[id(old_variable)] = new_variable
            existing_captures.add(id(old_variable.handle))

    for old_variable in local_collection_variables:
        if _should_lift_variable(old_variable):
            new_variable = _lift_single_variable(
                old_variable, graph, variable_holder)
            lifted_variables[id(old_variable)] = new_variable
            existing_captures.add(id(old_variable.handle))
            if new_variable._in_graph_mode:  # pylint: disable=protected-access
                outer_graph = new_variable.graph
                # Variables are added to the global collection by default. In this
                # case we only want the variable in the local collection, so we'll pop
                # it out.
                global_collection = outer_graph.get_collection_ref(
                    ops.GraphKeys.GLOBAL_VARIABLES)
                global_collection.remove(new_variable)
                outer_graph.add_to_collection(
                    ops.GraphKeys.LOCAL_VARIABLES, new_variable)

    # Update the FuncGraph's collections, partly for the user and partly so this
    # function is idempotent when it runs again in prune() calls.
    for collection_name in [
        ops.GraphKeys.GLOBAL_VARIABLES, ops.GraphKeys.LOCAL_VARIABLES
    ]:
        mutable_collection = ops.get_collection_ref(collection_name)
        for index, current in enumerate(mutable_collection):
            mutable_collection[index] = lifted_variables.get(id(current), current)
            if not resource_variable_ops.is_resource_variable(
                mutable_collection[index]):
                logging.log_first_n(
                    logging.WARN,
                    "Unable to create a python object for variable {} because it is "
                    "a reference variable. It may not be visible to training APIs. "
                    "If this is a problem, consider rebuilding the SavedModel after "
                    "running tf.compat.v1.enable_resource_variables().".format(
                        mutable_collection[index]),
                    5)
