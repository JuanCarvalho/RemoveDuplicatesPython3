#!/usr/bin/env python
# coding=utf-8
# remove-duplicates.py: deletes files (and images) which have duplicate size
#                       and md5sum
# by dpt
# Remove arquivos com conteudos identicos (Também serve para imagens)
# code adapted by juancarvalho for use with Python 3.5.2 (for personal use)
# link original http://www.davespace.co.uk/python/remove-duplicates.html (python 2.7)

import os
import hashlib
import stat
import sys



class RemoveImagensDuplicadas():

    """
        Usage when imported:
        from RemoveDuplicatesPython3 import RemoveImagensDuplicadas
        obj_rmv = RemoveImagensDuplicadas()
        obj_rmv.main('Path/To/Folder', cmdline=False)
        
    """

    Ignore = ('Thumbs.db',)

    def getmd5(self, filename):
        m = hashlib.md5()
        m.update(open(filename, 'rb').read(-1))
        return m.hexdigest()

    def usage(self):
        print('Usage: remove-duplicates.py DIRECTORY')
        sys.exit(1)

    def main(self, argv, cmdline=True):
        """
            argv = ['path/to/dir']
            cmdline=False # Use when > from remove-duplicates import RemoveImagensDuplicadas
        """
        if len(argv) < 1:
            self.usage()

        if argv[0] == '-h' or argv[0] == '--help':
            self.usage()

        dir = os.path.abspath(argv[0])

        # if imported in other script
        if not cmdline:
            dir = os.path.abspath(argv)

        print('Reading sizes...')
        # Create a dictionary keyed by size, with each entry holding a list of
        # filenames of that size.
        data = {}
        for root, dirs, files in os.walk(dir):
            for name in files:
                if name in self.Ignore: continue
                path = os.path.join(root, name)
                size = os.path.getsize(path)
                if not size in data:
                    data[size] = []

                data[size].append(path)

        # For each key, checksum each list entry and compare.

        removed = 0

        for k in data.keys():
            dk = data[k]
            if len(dk) > 1:
                #print(k, len(dk))
                s = {}
                for j in dk:
                    sum = self.getmd5(j)
                    if sum in s:
                        print(j, 'is a dupe of', s[sum])
                        try:
                            os.remove(j)
                            removed += 1
                        except:
                            pass
                    else:
                        s[sum] = j

        print('Done, %d files removed.' % (removed))

if __name__ == '__main__':
    RemoveImagensDuplicadas().main(sys.argv[1:])