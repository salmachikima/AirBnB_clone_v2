#!/usr/bin/python3
""" script that distributes an archive to your web servers based on task 1"""


from fabric.api import *
from datetime import datetime


def do_pack():
    """ destribute archive to the webservers"""
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    result = local("sudo tar -cvzf {} web_static".format(filename))
    if result.succeeded:
        return filename
    else:
        return None
