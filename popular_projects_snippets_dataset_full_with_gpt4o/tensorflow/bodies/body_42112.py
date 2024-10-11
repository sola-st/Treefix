# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/resnet50_test.py
optimizer.apply_gradients(zip(gradients, model.variables))
