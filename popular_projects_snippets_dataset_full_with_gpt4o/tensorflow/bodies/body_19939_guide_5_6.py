# Define a class to encapsulate the code snippet and execute it # pragma: no cover
class EmbeddingVariable: # pragma: no cover
    def get_embedding_variable_name(self): # pragma: no cover
        """Returns the embedding variable name. # pragma: no cover
        Feature key name and embedding variable name are usually one-to-one mapping. # pragma: no cover
        But for shared embedding columns, it is many-to-one mapping. # pragma: no cover
        """ # pragma: no cover
        raise NotImplementedError('not impl') # pragma: no cover
 # pragma: no cover
# Create an instance of the class and call the method to execute the code snippet # pragma: no cover
try: # pragma: no cover
    embedding_var = EmbeddingVariable() # pragma: no cover
    embedding_var.get_embedding_variable_name() # pragma: no cover
except NotImplementedError as e: # pragma: no cover
    print(e) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column.py
from l3.Runtime import _l_
"""Returns the embedding variable name.

    Feature key name and embedding variable name are usually one-to-one mapping.
    But for shared embedding columns, it is many-to-one mapping.
    """
raise NotImplementedError('not impl')
_l_(18511)
