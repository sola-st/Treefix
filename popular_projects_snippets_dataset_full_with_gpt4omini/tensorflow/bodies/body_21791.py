# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
exit((data_flow_ops.PaddingFIFOQueue if dynamic_pad
        else data_flow_ops.FIFOQueue))
