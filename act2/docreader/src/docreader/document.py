from pathlib import Path
import mimetypes
from abc import ABC, abstractmethod

class Document(ABC):
    def __init__(self, filepath: Path):
        self.filepath = filepath

    @property
    def mime_type(self) -> tuple[str|None, str|None]:
        """Returns a tuple of the form (mimetype, encoding). If either the type or the encoding
        cannot be guessed the value will be None."""
        return mimetypes.guess_type(self.filepath)

    @abstractmethod
    def text(self) -> str:
        pass

    @abstractmethod
    def author(self) -> str:
        pass
