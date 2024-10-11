# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Create embedding and slot variables, with ops to load and retrieve them.

    N.B.: the retrieve embedding variables (including slot variables) ops are
    returned as lambda fn, as the call side might want to impose control
    dependencies between the TPU computation and retrieving actions. For
    example, the following code snippet ensures the TPU computation finishes
    first, and then we pull the variables back from TPU to CPU.

    ```
    updates_ops = []
    with ops.control_dependencies([loss]):
      for op_fn in retrieve_parameters_op_fns:
        update_ops.append(op_fn())
    ```

    Args:
      embedding_variable_name_by_table: A dictionary mapping from string of
        table name to string of embedding variable name. If `None`, defaults
        from `get_default_slot_variable_names()` will be used.
      slot_variable_names_by_table: A dictionary mapping from string of table
        name to `AdamSlotVariableNames`, `AdagradSlotVariableNames` etc. If
        `None`, defaults from `get_default_slot_variable_names()` will be used.

    Returns:
      `tpu_embedding.VariablesAndOps` with:
        A dictionary mapping from string of table name to embedding variables,
        A dictionary mapping from string of table name to AdagradSlotVariables,
         AdamSlotVariables etc with slot variables,
        A function which returns a list of ops to load embedding and slot
         variables from CPU to TPU.
        A function which returns a list of ops to retrieve embedding and slot
         variables from TPU to CPU.
    """
embedding_variables_by_table = {}
slot_variables_by_table = {}
load_op_fns = []
retrieve_op_fns = []

for i, table in enumerate(self._table_to_config_dict):
    if embedding_variable_name_by_table:
        embedding_variable_name = embedding_variable_name_by_table[table]
    else:
        embedding_variable_name = table
    if slot_variable_names_by_table:
        slot_variable_names = slot_variable_names_by_table[table]
    else:
        optimizer_handler = self._optimizer_handler_dict[table]
        slot_variable_names = (
            optimizer_handler.get_default_slot_variable_names(table))

    # TODO(b/139144091): Multi-host support for mid-level API in
    #  eager context (TF 2.0)
    # Workaround below allows single-host use case in TF 2.0
    if context.executing_eagerly():
        device = ''
    else:
        device = _create_device_fn(self._hosts)

    with ops.device(device):
        table_variables = _create_partitioned_variables(
            name=embedding_variable_name,
            num_hosts=self._num_hosts,
            vocabulary_size=self._table_to_config_dict[table].vocabulary_size,
            embedding_dimension=self._table_to_config_dict[table].dimension,
            initializer=self._table_to_config_dict[table].initializer,
            collections=[ops.GraphKeys.GLOBAL_VARIABLES])
        embedding_variables_by_table[table] = table_variables

        # Only loads embedding config to load/retrieve nodes for the first table
        # on the first host, other nodes would use config from the first node.
        config = None if i else self.config_proto.SerializeToString()
        slot_variables_for_table, load_ops_fn, retrieve_ops_fn = (
            self._optimizer_handler_dict[table].create_variables_and_ops(
                table, slot_variable_names, self._num_hosts,
                self._table_to_config_dict[table], table_variables, config))
        slot_variables_by_table[table] = slot_variables_for_table
        load_op_fns.append(load_ops_fn)
        retrieve_op_fns.append(retrieve_ops_fn)

def load_ops():
    """Calls and returns the load ops for each embedding table.

      Returns:
        A list of ops to load embedding and slot variables from CPU to TPU.
      """
    load_ops_list = []
    for load_op_fn in load_op_fns:
        load_ops_list.extend(load_op_fn())
    exit(load_ops_list)

def retrieve_ops():
    """Calls and returns the retrieve ops for each embedding table.

      Returns:
        A list of ops to retrieve embedding and slot variables from TPU to CPU.
      """
    retrieve_ops_list = []
    for retrieve_op_fn in retrieve_op_fns:
        retrieve_ops_list.extend(retrieve_op_fn())
    exit(retrieve_ops_list)

exit(VariablesAndOps(embedding_variables_by_table,
                       slot_variables_by_table, load_ops, retrieve_ops))
