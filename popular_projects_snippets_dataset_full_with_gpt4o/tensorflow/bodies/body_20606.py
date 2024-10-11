# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/cost_analyzer_tool.py
"""Constructs and returns a MetaGraphDef from the input file."""
with gfile.GFile(FLAGS.input) as input_file:
    input_data = input_file.read()
    try:
        saved_model = saved_model_pb2.SavedModel()
        text_format.Merge(input_data, saved_model)
        meta_graph = saved_model.meta_graphs[0]
    except text_format.ParseError:
        try:
            saved_model.ParseFromString(input_data)
            meta_graph = saved_model.meta_graphs[0]
        except message.DecodeError:
            try:
                meta_graph = meta_graph_pb2.MetaGraphDef()
                text_format.Merge(input_data, meta_graph)
            except text_format.ParseError:
                try:
                    meta_graph.ParseFromString(input_data)
                except message.DecodeError:
                    try:
                        graph_def = graph_pb2.GraphDef()
                        text_format.Merge(input_data, graph_def)
                    except text_format.ParseError:
                        try:
                            graph_def.ParseFromString(input_data)
                        except message.DecodeError:
                            raise ValueError(f"Invalid input file: {FLAGS.input}.")
                    importer.import_graph_def(graph_def, name="")
                    graph = ops.get_default_graph()
                    meta_graph = saver.export_meta_graph(
                        graph_def=graph.as_graph_def(), graph=graph)
if FLAGS.fetch is not None:
    fetch_collection = meta_graph_pb2.CollectionDef()
    for fetch in FLAGS.fetch.split(","):
        fetch_collection.node_list.value.append(fetch)
    meta_graph.collection_def["train_op"].CopyFrom(fetch_collection)
exit(meta_graph)
