#!/usr/bin/python3
""" This module generates a .tgz archive from """
from fabric.api import *
import datetime


def do_pack():
    """ Create pack of file .pgz """
    date_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    name_file = "versions/web_static_" + date_time + ".tgz"
    localpth = "web_static/"
    local("mkdir -p versions")
    result = local("tar -zcvf {} {}".format(name_file, localpth))
    if result is None:
        return None
    else:
        return name_file
