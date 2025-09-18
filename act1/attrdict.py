class AttrDict(dict):
    def __init__(self):
        super().__init__()
   
    def __setattr__(self, key, value) -> None:
        super().__setitem__(key, value)

    def __getattr__(self, key) -> any:
        return super().__getitem__(key)

