#! python3
# search_files - Search for a regular expression in all files inside a folder

import os, re
from .colors import color
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

class SearchFiles:
    'Search for a regular expression in all files inside a folder'

    def __init__(self, folder, regex):
        self.folder = folder
        self.regex = regex
        self.files = {}
        self.total_matches_files = 0
        self.total_matches = 0
        self.run()

    def txt(self, fname):
        try:
            text_file = open(fname, 'r')
            content = text_file.read()
        except:
            print(color.FAIL)
            print('Error reading file: ' + fname + color.ENDC)
            return None
        text_file.close()
        return content

    def pdf(self, fname, pages=None):
        if not pages:
            pagenums = set()
        else:
            pagenums = set(pages)

        output = StringIO()
        manager = PDFResourceManager()
        converter = TextConverter(manager, output, laparams=LAParams())
        interpreter = PDFPageInterpreter(manager, converter)

        infile = open(fname, 'rb')
        for page in PDFPage.get_pages(infile, pagenums):
            interpreter.process_page(page)
        infile.close()
        converter.close()
        text = output.getvalue()
        output.close()
        return text

    def run(self):
        files = os.listdir(self.folder)
        for file in files:
            if os.path.splitext(file)[1] == '.pdf':
                content = self.pdf(file)
            else:
                content = self.txt(file)

            if content is not None:
                found = len(re.compile(self.regex).findall(content))
                self.files.setdefault(file, found)
                if found > 0:
                    self.total_matches_files += 1
                    self.total_matches += found
