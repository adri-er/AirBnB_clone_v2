#!/usr/bin/python3
""" This module generates a .tgz archive from """
from fabric import local
import datetime


def do_pack():
    """ Create pack of file .pgz """
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    name_file = "web_static_" + date_time + ".tgz"
    localpth = "/AirBnB_clone_v2/web_static"
    result = local("tar -zcvf {} {}".format(name_file, localpth))
    if result is None:
        return None
    else:
        return name_file
