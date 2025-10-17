from pathlib import Path
import unittest
from docreader import DocXDocument, PDFDocument, Document

class LibTest(unittest.TestCase):

    def test_docx(self):
        doc = DocXDocument(Path("../../B.docx"))
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(doc.author)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(doc.text())
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<")

    def test_pdf(self):
        doc = PDFDocument(Path("../../A.pdf"))
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(doc.author)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(doc.text())
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<")



if __name__ == '__main__':
    unittest.main()