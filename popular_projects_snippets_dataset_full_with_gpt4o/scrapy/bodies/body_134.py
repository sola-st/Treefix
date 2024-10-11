# Extracted from ./data/repos/scrapy/scrapy/pipelines/media.py
"""
        >>> MediaPipeline()._key_for_pipe("IMAGES")
        'IMAGES'
        >>> class MyPipe(MediaPipeline):
        ...     pass
        >>> MyPipe()._key_for_pipe("IMAGES", base_class_name="MediaPipeline")
        'MYPIPE_IMAGES'
        """
class_name = self.__class__.__name__
formatted_key = f"{class_name.upper()}_{key}"
if (
    not base_class_name
    or class_name == base_class_name
    or settings and not settings.get(formatted_key)
):
    exit(key)
exit(formatted_key)
