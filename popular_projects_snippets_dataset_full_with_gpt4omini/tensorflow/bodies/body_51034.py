# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_impl.py
"""Loads the model from a SavedModel as specified by tags.

  Args:
    sess: The TensorFlow session to restore the variables.
    tags: Set of string tags to identify the required MetaGraphDef. These should
        correspond to the tags used when saving the variables using the
        SavedModel `save()` API.
    export_dir: Directory in which the SavedModel protocol buffer and variables
        to be loaded are located.
    import_scope: Optional `string` -- if specified, prepend this string
        followed by '/' to all loaded tensor names. This scope is applied to
        tensor instances loaded into the passed session, but it is *not* written
        through to the static `MetaGraphDef` protocol buffer that is returned.
    **saver_kwargs: Optional keyword arguments passed through to Saver.

  Returns:
    The `MetaGraphDef` protocol buffer loaded in the provided session. This
    can be used to further extract signature-defs, collection-defs, etc.

  Raises:
    RuntimeError: MetaGraphDef associated with the tags cannot be found.

  @compatibility(TF2)

  `tf.compat.v1.saved_model.load` or `tf.compat.v1.saved_model.loader.load` is
  not compatible with eager execution. Please use `tf.saved_model.load` instead
  to load your model. You can refer to the [SavedModel guide]
  (https://www.tensorflow.org/guide/saved_model) for more information as well as
  "Importing SavedModels from TensorFlow 1.x" in the [`tf.saved_model.load`]
  (https://www.tensorflow.org/api_docs/python/tf/saved_model/load) docstring.

  #### How to Map Arguments

  | TF1 Arg Name          | TF2 Arg Name    | Note                       |
  | :-------------------- | :-------------- | :------------------------- |
  | `sess`                | Not supported   | -                          |
  | `tags`                | `tags`          | -                          |
  | `export_dir`          | `export_dir`    | -                          |
  | `import_scope`        | Not supported   | Name scopes are not needed.
  :                       :                 : By default, variables are  :
  :                       :                 : associated with the loaded :
  :                       :                 : object and function names  :
  :                       :                 : are deduped.               :
  | `saver_kwargs`        | Not supported   | -                          |

  #### Before & After Usage Example

  Before:

  ```
  with tf.compat.v1.Session(graph=tf.Graph()) as sess:
    tf.compat.v1.saved_model.loader.load(sess, ["foo-tag"], export_dir)
  ```

  After:

  ```
  model = tf.saved_model.load(export_dir, tags=["foo-tag"])
  ```
  @end_compatibility
  """
loader = SavedModelLoader(export_dir)
exit(loader.load(sess, tags, import_scope, **saver_kwargs))
