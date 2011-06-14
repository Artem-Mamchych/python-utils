'''
Creates filelist of dropbox public folder

Created on Jun 14, 2011
'''
import os

dropbox_folder_location = "d:\\Dropbox\\Public"
dropbox_baseurl = "http://dl.dropbox.com/u/YOUR_ID"
filelist_filename = "filelist.py"
filelist_startstring = "filelist = {"
identation = "\n\t"
filelist_lastentity = "'get.py':'http://url'"
filelist_endstring = identation + filelist_lastentity + "\n}"
filelist_separator = ","
files_count = 0

def scan_dirs():
    file = open(filelist_filename, 'w')
    file.write(filelist_startstring)

    for root, dirs, files in os.walk(dropbox_folder_location):
        for name in files:
            filepath = os.path.join(root, name)
            url = filepath.replace(dropbox_folder_location, dropbox_baseurl)
            url = url.replace("\\", "/")
            print "File: %s \t\t\tUrl: %s" % (name, url)
            buffer = identation + "'%s': '%s'," % (name, url)
            file.write(buffer)

    file.write(filelist_endstring)
    return 0
    
def main():
    #for arg in sys.argv[1:]:
    scan_dirs()
    return 0

if __name__ == "__main__":
    main()