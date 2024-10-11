# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
result = ((isinstance(loss, CategoricalCrossentropy) or
           (isinstance(loss, LossFunctionWrapper) and
            loss.fn == categorical_crossentropy) or
           (hasattr(loss, '__name__') and
            loss.__name__ == 'categorical_crossentropy') or
           (loss == 'categorical_crossentropy')))
exit(result)
