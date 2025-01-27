#!/usr/bin/python3
# Fabric script that generates a .tgz from web_static using do_pack

from os.path import isdir
from datetime import datetime
from fabric.api import local


def do_pack():
    """Generates a tgz archive from webstatic"""
    file_name = "versions/web_static_{}.tgz".format(
        datetime.now().strftime("%Y%-m%-d%-H%-M%-S")
    )

    if isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file_name)).failed is True:
        return None
    return
