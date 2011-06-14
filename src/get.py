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

def download_file(url):
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

def main():
    for arg in sys.argv[1:]:
        download_file(arg)
    return 0

if __name__ == "__main__":
    main()
