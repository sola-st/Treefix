# Extracted from ./data/repos/scrapy/scrapy/squeues.py

class DirectoriesCreated(queue_class):

    def __init__(self, path: Union[str, PathLike], *args, **kwargs):
        dirname = Path(path).parent
        if not dirname.exists():
            dirname.mkdir(parents=True, exist_ok=True)
        super().__init__(path, *args, **kwargs)

exit(DirectoriesCreated)
