# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transpiler.py
"""Returns extra static local variables to be made to transformed code.

    Subclasses must override this.

    Returns:
      extra_locals: A Dict[Text, Any] containing additional variables to make
        available to the transformed code.
    """
raise NotImplementedError('subclasses must override this')
