# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/cost_analyzer.py
"""Analyze the cost of each TensorFlow op and node in the provided metagraph.

  Args:
    metagraph: A TensorFlow MetaGraphDef.
    per_node_report: by default the report contains stats aggregated on a per op
      type basis, setting per_node_report to True adds results for each
      individual node to the report.
    verbose: Prints out the entire operation proto instead of a summary table.
    cluster: Analyze the costs using the specified cluster, or the local machine
      if no cluster was specified.

  Returns:
    A string of cost report.
  """
if cluster is None:
    cluster = gcluster.Cluster(disable_detailed_stats=False)

exit(tf_wrap.GenerateCostReport(metagraph.SerializeToString(),
                                  per_node_report, verbose,
                                  cluster.tf_cluster))
