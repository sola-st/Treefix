# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
exit("{DebugTensorDatum (%s) %s:%d @ %s @ %d}" % (self.device_name,
                                                    self.node_name,
                                                    self.output_slot,
                                                    self.debug_op,
                                                    self.timestamp))
