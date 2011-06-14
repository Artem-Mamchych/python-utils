'''
get.py is lightweight wget replacement.
Usage: get.py file_url_1 file_url_2 file_url_N 
Created on Jun 14, 2011
License: BSD

TODO: replace all %20 by spaces
TODO: fix progress counter
TODO: if argument not starts with http:// etc - download file from dropbox
repository = {"alias1":"file_url1"}
'''
import urllib2
import sys

filelist_url = "http://dl.dropbox.com/u/21385319/config/filelist.py"
filelist = {
            'switchall': "http://dl.dropbox.com/u/21385319/build/switch-all.bat",
            'build': "http://dl.dropbox.com/u/21385319/build/pim-eclipse.txt"
            }

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
        if file_size > block_sz:
            status = r"%10d  [%3.0f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            print status,

    f.close()
    return 0

def download_filelist():
    print "Downloads filelist"
    return 0

def resolve_file(alias):
    print "Resolves files by given alias name from filelist dictionary"
    if alias in filelist:
        print "alias found"
    return 0

#Downloads or Resolves file
#Order:
#1. if filepath starts with http:// or etc - try download_file(filepath)
#2. otherwise - search in filelist for alias and download_file(filelist.get(filepath))
#3. if not in filelist - try download_file()
def get_file(filepath):
    if not (filepath.startswith("http://") or filepath.startswith("www.") or filepath.startswith("ftp://")):
        if filepath in filelist:
            print "%s found in filelist: %s" % (filepath, filelist.get(filepath))
        else:
            print "%s not found in filelist" % (filepath)
    else:
        download_file(filepath)
        #check for errors
    return 0

def main():
    for arg in sys.argv[1:]:
        get_file(arg)
    return 0

if __name__ == "__main__":
    main()
