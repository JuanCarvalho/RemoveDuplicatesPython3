# RemoveDuplicatesPython3
Remove arquivos com conteudos identicos (também serve para imagens) 

Removes files with identical contents (also for images)

### code adapted by juancarvalho for use with Python 3.5.2 (for personal use)
### link original http://www.davespace.co.uk/python/remove-duplicates.html (python 2.7)

# Usage in terminal:
RemoveDuplicatesPython3.py Folder/

# importing into another script:

from RemoveDuplicatesPython3 import RemoveImagensDuplicadas

obj_rmv = RemoveImagensDuplicadas()

obj_rmv.main('Path/To/Folder', cmdline=False)
