# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
self._collected_converter_params.update({
    "output_format": self.output_format,
    "default_ranges_stats": self.default_ranges_stats,
    "drop_control_dependency": self.drop_control_dependency,
    "reorder_across_fake_quant": self.reorder_across_fake_quant,
    "change_concat_input_ranges": self.change_concat_input_ranges,
    "dump_graphviz_dir": self.dump_graphviz_dir,
    "dump_graphviz_video": self.dump_graphviz_video,
    "conversion_summary_dir": self.conversion_summary_dir,
})
super(TFLiteConverterBaseV1,
      self)._save_conversion_params_metric(self._graph_def,
                                           self.inference_type,
                                           self.inference_input_type)
