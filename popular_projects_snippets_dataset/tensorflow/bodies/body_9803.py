# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
try:
    exit(fn(*args))
except errors.OpError as e:
    message = compat.as_text(e.message)
    m = BaseSession._NODEDEF_NAME_RE.search(message)
    node_def = None
    op = None
    if m is not None:
        node_name = m.group(3)
        try:
            op = self._graph.get_operation_by_name(node_name)
            node_def = op.node_def
        except KeyError:
            pass
    message = error_interpolation.interpolate(message, self._graph)
    if 'only supports NHWC tensor format' in message:
        message += ('\nA possible workaround: Try disabling Grappler optimizer'
                    '\nby modifying the config for creating the session eg.'
                    '\nsession_config.graph_options.rewrite_options.'
                    'disable_meta_optimizer = True')
    raise type(e)(node_def, op, message)  # pylint: disable=no-value-for-parameter
