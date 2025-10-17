from .document import Document
from pathlib import Path
import pdfplumber

class PDFDocument(Document):
    def __init__(self, filepath: Path):
        super().__init__(filepath)
        self.document = pdfplumber.open(self.filepath)

    @property
    def author(self) -> str:
        return self.document.metadata.get("Author", "")

    def text(self) -> str:
        return "\n".join(page.extract_text_simple() for page in self.document.pages)