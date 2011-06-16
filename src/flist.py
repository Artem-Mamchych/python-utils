'''
Creates filelist of dropbox public folder

Created on Jun 14, 2011
'''
import sys
import os
import json

#[-f filelist_filename]
helpstring = "%s saves directory tree to json file.\n Usage: %s directory [base_url] \
N\nOptions\
\n\t-v\tPrints version info \
\n\t-h\tPrints this help message \
" % (sys.argv[0], sys.argv[0])

version = 0.1
latestversion_url = "https://raw.github.com/TQFP64/python-utils/master/src/flist.py"
versionstring = "%s version: %s  Latest version avalible at:\n %s" % (sys.argv[0], version, latestversion_url)

dir_separator = "\\"
dropbox_folder_marker = "Public"
dropbox_baseurl = "http://dl.dropbox.com/u/21385319"
filelist_filename = "filelist.json"
files_count = 0

def scan_dirs(directory):
    filelist = {}
    file = open(filelist_filename, 'w')

    for root, dirs, files in os.walk(directory):
        for name in files:
            filepath = os.path.join(root, name)
            if directory.endswith(dropbox_folder_marker) or directory.endswith(dropbox_folder_marker + dir_separator):
                url = filepath.replace(directory, dropbox_baseurl)
                filepath = url.replace("\\", "/")
                
            print "File: %s \t\tUrl: %s" % (name, filepath)
            if not filelist.has_key(name):
                filelist[name] = filepath

    json.dump(filelist, file)
    return 0

"""
Parses current option and runs its action, returns True
If argument not an option returns False 
"""
def option(option):
    if option == "-h":
        print helpstring
    elif option == "-v":
        print versionstring
    else:
        return False 
    return True

def main():
    for arg in sys.argv[1:]:
        if not option(arg):
            scan_dirs(arg)
    return 0

if __name__ == "__main__":
    main()