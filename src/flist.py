'''
Creates filelist of dropbox public folder

Created on Jun 14, 2011
'''
import os
import json

dropbox_folder_location = "d:\\Dropbox\\Public"
dropbox_baseurl = "http://dl.dropbox.com/u/YOUR_ID"
filelist_filename = "filelist.json"
files_count = 0

def scan_dirs():
    filelist = {}
    file = open(filelist_filename, 'w')

    for root, dirs, files in os.walk(dropbox_folder_location):
        for name in files:
            filepath = os.path.join(root, name)
            url = filepath.replace(dropbox_folder_location, dropbox_baseurl)
            url = url.replace("\\", "/")
            print "File: %s \t\tUrl: %s" % (name, url)
            if not filelist.has_key(name):
                filelist[name] = [url]

    json.dump(filelist, file)
    return 0

def main():
    scan_dirs()
    return 0

if __name__ == "__main__":
    main()