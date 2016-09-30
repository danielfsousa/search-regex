#! python3
# search_regex - Search for a regular expression in all files inside a folder

import sys, os
from modules.search_files import SearchFiles
from modules.colors import color

if len(sys.argv) != 3:
    print('\nUsage:')
    print('        python regex_search_txt [FOLDER] [REGEX]  =>  Search regex in all txt files inside the given folder')
    print('        python regex_search_txt -c [REGEX]        =>  Search regex in all txt files inside the current folder')
    print('\nDon\'t forget to use " between the [REGEX]')
else:
    if sys.argv[1] == '-c':
        result = SearchFiles(os.getcwd(), sys.argv[2])
    elif os.path.isdir(sys.argv[1]):
        result = SearchFiles(sys.argv[1], sys.argv[2])
    else:
        print(color.FAIL)
        print('\nCannot find the directory')
        print(color.ENDC)
        sys.exit()

    for key, val in result.files.items():
        if val > 0:
            print(color.OKGREEN)
        else:
            print(color.FAIL)

        print('Found ' + str(val) + ' matches in ' + key + color.ENDC)

    print('\n----------------------------------')
    print(color.WARNING)
    print('Found ' + str(result.total_matches) + ' matches in ' + str(result.total_matches_files) + ' files.')
    print(color.ENDC)