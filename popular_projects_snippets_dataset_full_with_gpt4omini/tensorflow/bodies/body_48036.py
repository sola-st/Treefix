# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/sequential.py
for ref_layer in self.layers:
    if layer.name == ref_layer.name and ref_layer is not layer:
        exit(False)
exit(True)
