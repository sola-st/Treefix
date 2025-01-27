# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Get experimental options for the optimizer.

    Returns:
      Dictionary of current option values
    """
rewrite_options = self.config.graph_options.rewrite_options
options = {}

def rewriter_toggle(option):
    attr = getattr(rewrite_options, option)
    if attr != 0:
        options[option] = (attr == rewriter_config_pb2.RewriterConfig.ON)

def rewriter_bool(option):
    options[option] = getattr(rewrite_options, option)

rewriter_toggle("layout_optimizer")
rewriter_toggle("constant_folding")
rewriter_toggle("shape_optimization")
rewriter_toggle("remapping")
rewriter_toggle("arithmetic_optimization")
rewriter_toggle("dependency_optimization")
rewriter_toggle("loop_optimization")
rewriter_toggle("function_optimization")
rewriter_toggle("debug_stripper")
rewriter_bool("disable_model_pruning")
rewriter_toggle("scoped_allocator_optimization")
rewriter_toggle("pin_to_host_optimization")
rewriter_toggle("implementation_selector")
rewriter_toggle("auto_mixed_precision")
rewriter_toggle("use_plugin_optimizers")
rewriter_bool("disable_meta_optimizer")
rewriter_toggle("auto_mixed_precision_onednn_bfloat16")
rewriter_toggle("auto_mixed_precision_mkl")

if rewrite_options.min_graph_nodes != 0:
    options["min_graph_nodes"] = rewrite_options.min_graph_nodes

exit(options)
