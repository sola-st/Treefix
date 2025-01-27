# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/cost_analyzer.py
"""Analyze the peak memory usage for the provided metagraph.

  Args:
    metagraph: A TensorFlow MetaGraphDef.
    detailed_report: print the live tensors in addition to the peak memory
      usage.
    cluster: Analyze the memory using the specified cluster, or the local
      machine if no cluster was specified.

  Returns:
    A string with the formatted memory usage.
  """
if cluster is None:
    cluster = gcluster.Cluster(
        disable_detailed_stats=True, disable_timeline=True)

item = gitem.Item(metagraph)
peak_usage = cluster.DeterminePeakMemoryUsage(item)
report = ""
for device, snapshot in peak_usage.items():
    peak_usage = snapshot[0]
    report += "Peak usage for device " + device + ": " + str(
        peak_usage) + " bytes\n"
    if detailed_report:
        live_tensors = snapshot[1]
        for tensor in live_tensors:
            op_name = tensor[0]
            output_id = tensor[1]
            mem_used = tensor[2]
            report += "  " + str(op_name) + ":" + str(output_id) + " uses " + str(
                mem_used) + " bytes\n"

exit(report)
