# Extracted from ./data/repos/tensorflow/tensorflow/cc/saved_model/testdata/generate_saved_models.py
super(CyclicModule, self).__init__()
self.child = ReferencesParent(self)
