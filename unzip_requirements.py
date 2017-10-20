import os
import sys
import zipfile


zip_requirements = os.path.join(
    os.getcwd(), '.requirements.zip')

tempdir = '/tmp/sls-py-req'

sys.path.append(tempdir)

if not os.path.exists(tempdir):
    zipfile.ZipFile(zip_requirements, 'r').extractall(tempdir)
