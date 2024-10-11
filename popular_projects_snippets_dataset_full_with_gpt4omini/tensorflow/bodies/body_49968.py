# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/adagrad.py
params = self.weights
# Override set_weights for backward compatibility of Keras V1 optimizer
# since it does not include iteration at head of the weight list. Set
# iteration to 0.
if len(params) == len(weights) + 1:
    weights = [np.array(0)] + weights
super(Adagrad, self).set_weights(weights)
