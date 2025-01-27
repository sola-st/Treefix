# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer.py
"""Removes unknown default attrs according to `producer_op_list`.

  Removes any unknown attrs in `graph_def` (i.e. attrs that do not appear in
  registered OpDefs) that have a default value in `producer_op_list`.

  Args:
    producer_op_list: OpList proto.
    graph_def: GraphDef proto
  """
producer_op_dict = {op.name: op for op in producer_op_list.op}
for node in graph_def.node:
    # Remove any default attr values that aren't in op_def.
    if node.op in producer_op_dict:
        op_def = op_def_registry.get(node.op)
        if op_def is None:
            # Some custom op registrations won't show up here. That's OK, attribute
            # stripping just won't be available.
            continue
        producer_op_def = producer_op_dict[node.op]
        # We make a copy of node.attr to iterate through since we may modify
        # node.attr inside the loop.
        for key in list(node.attr):
            if _FindAttrInOpDef(key, op_def) is None:
                # No attr_def in consumer, look in producer.
                attr_def = _FindAttrInOpDef(key, producer_op_def)
                if (attr_def and attr_def.HasField('default_value') and
                    node.attr[key] == attr_def.default_value):
                    # Unknown attr had default value in producer, delete it so it can be
                    # understood by consumer.
                    del node.attr[key]
