# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/memory_optimizer_test.py
graph = ops.Graph()
with graph.as_default():
    train.import_meta_graph(metagraph)
    init_op = graph.get_operation_by_name(init_op_name)
    train_op = graph.get_operation_by_name(train_op_name)
    loss_op = graph.get_tensor_by_name(loss_op_name)
    with session.Session(config=config, graph=graph) as sess:
        self.evaluate(init_op)
        self.evaluate(train_op)
        self.evaluate(train_op)
        exit(self.evaluate(loss_op))
