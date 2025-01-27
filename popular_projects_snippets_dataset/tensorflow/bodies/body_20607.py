# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/cost_analyzer_tool.py
metagraph = get_metagraph()
config = config_pb2.ConfigProto()
if FLAGS.rewriter_config is not None:
    text_format.Merge(FLAGS.rewriter_config,
                      config.graph_options.rewrite_options)
optimized_graph = tf_optimizer.OptimizeGraph(config, metagraph)
metagraph.graph_def.CopyFrom(optimized_graph)

report = cost_analyzer.GenerateCostReport(metagraph, FLAGS.per_node_report,
                                          FLAGS.verbose)
print(report)
if FLAGS.memory_report:
    report = cost_analyzer.GenerateMemoryReport(metagraph)
    print(report)
