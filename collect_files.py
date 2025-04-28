import sys
import os
import shutil

src = sys.argv[1]
dst = sys.argv[2]

if not os.path.isdir(src):

    sys.exit(1)

if not os.path.exists(dst):
    os.mkdir(dst)

for dirpath, dirnames, filenames in os.walk(src):
    for name in filenames:
        full_path = os.path.join(dirpath, name)
        shutil.copy(full_path, dst)
