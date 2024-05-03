#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the contents of the web_static
folder.
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static folder.

    Returns:
        The archive path if the archive has been correctly generated.
        None otherwise.
    """
    try:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception:
        return None
