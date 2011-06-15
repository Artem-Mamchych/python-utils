'''
get.py is lightweight wget replacement.
Usage: get.py file_url_1 file_url_2 file_url_N 
Created on Jun 14, 2011
License: BSD

TODO: replace all %20 by spaces
TODO: setting filelist download url; -f use filelist with specified name;
 -s=name search alias which contains 'name' ; auto-download filelist
'''
import urllib2
import sys
import os.path
import json

helpstring = "get.py is lightweight wget replacement.\n Usage: %s [-p] [-v] [-h] \
url1 url2 urlN\nOptions\
\n\t-p\tPrints filelist content as 'alias' = 'url' pairs \
\n\t-v\tPrints version info \
\n\t-h\tPrints this help message \
" % sys.argv[0]

version = 0.1
latestversion_url = "https://raw.github.com/TQFP64/python-utils/master/src/get.py"
versionstring = "%s version: %s  Latest version avalible at:\n %s" % (sys.argv[0], version, latestversion_url)
filelist_filename = "filelist.json"
filelist_url = "http://dl.dropbox.com/u/======/config/filelist.py"
filelist = {}

def download_file(url):
    #if not url.startswith("http://"):
    #url.insert(0, "http://")
    file_name = url.split('/')[-1]
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += block_sz
        f.write(buffer)
        persents_progress = file_size_dl * 100. / file_size
        if persents_progress > 100.:
            persents_progress = 100.
            file_size_dl = file_size
        if file_size > block_sz:
            status = r"%10d  [%3.0f%%]" % (file_size_dl, persents_progress)
            status = status + chr(8)*(len(status)+1)
            print status,

    f.close()
    return 0

def init_filelist():
    if os.path.isfile(filelist_filename):
        if os.path.exists(filelist_filename):
            try:
                dict = json.load(open(filelist_filename))
            except:
                print "ERROR OPENING JSON!"
                sys.exit(1)

    return dict

#Downloads or Resolves file
#Order:
#1. if filepath starts with http:// or etc - try download_file(filepath)
#2. otherwise - search in filelist for alias and download_file(filelist.get(filepath))
#3. if not in filelist - try download_file()
def get_file(filepath, filelist):
    if not (filepath.startswith("http://") or filepath.startswith("www.") or filepath.startswith("ftp://")):
        if filepath in filelist:
            print "%s found in filelist: %s" % (filepath, filelist.get(filepath))
            download_file(filelist.get(filepath))
        else:
            print "%s not found in filelist" % (filepath)
    else:
        download_file(filepath)
        #check for errors
    return 0

def download_filelist():
    print "Downloads filelist"
    return 0

"""
Parses current option and runs its action, returns True
If argument not an option returns False 
"""
def option(option, filelist):
    if option == "-p":
        for key in filelist:
            print "%s = %s" % (key, filelist[key])
    elif option == "-h":
        print helpstring
    elif option == "-v":
        print versionstring
    else :
        return False 
    return True    

def main():
    for arg in sys.argv[1:]:
        filelist = init_filelist()
        if not option(arg, filelist):
            get_file(arg, filelist)
    return 0

if __name__ == "__main__":
    main()
