# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test_utils.py
tensors = table._export()
specs = [
    saver_module.BaseSaverBuilder.SaveSpec(tensors[0], "",
                                           name + "-keys"),
    saver_module.BaseSaverBuilder.SaveSpec(tensors[1], "",
                                           name + "-values")
]
super(CheckpointedOp.CustomSaveable, self).__init__(table, specs, name)
