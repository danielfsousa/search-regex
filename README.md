# SearchRegex
Search for a regular expression in all files inside a folder

## Requirements
* [Python 3.x](https://www.python.org/downloads/)
* [PDFMiner.six](https://github.com/goulu/pdfminer)

## Supported Files
* All non-binary files like TXT, HTML, PHP, PY, etc.
* PDF

## How to Install
```bash
$ pip install pdfminer.six

TODO
```

## How to Use
**1. Use in command-line:**
* [FOLDER]: The folder where the files are located (You can use -c for the current folder)
* [REGEX]: The regular expression to find
```bash
$ python search_regex.py [FOLDER] [REGEX]
```

E.g. Find the word 'programming':
```bash
$ python search_regex.py -c "programming"
```

E.g. Find emails:
```bash
$ python search_regex.py -c ".+@.+"
```

**2. Use as a library:**

    result = SearchFiles(DIR, REGEX)
    found_files = result.files
    
E.g Find emails:
```bash
>>> import os
>>> from modules.search_files import SearchFiles
>>>
>>> result = SearchFiles(os.getcwd(), ".+@.+")
>>> result.files
{'telefone_e_email.py': 1, 'example.py': 1, 'personal_emails.txt': 3}
>>> result.total_matches
5
>>> result.total_matches_files
3
>>> result.folder
'C:\\example'
>>> result.regex
'.+@.+'
```

## TODO
* Package this project
* Add support for DOC and DOCX
* Add support for EPUB
* Add support for MOBI
* Add support for compressed files like ZIP or RAR
