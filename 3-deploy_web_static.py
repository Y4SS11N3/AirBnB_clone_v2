#!/usr/bin/python3
"""
Fabric script to create and distribute an archive to web servers.
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
import os

env.hosts = ['54.90.33.112', '23.23.75.134']
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static folder.

    Returns:
        The path to the generated archive.
    """
    try:
        if not isdir("versions"):
            local("mkdir versions")
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(current_time)
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except:
        return None


def do_deploy(archive_path):
    """
    Distribute an archive to web servers.

    Args:
        archive_path (str): The path of the archive to distribute.

    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not exists(archive_path):
        return False

    try:
        filename = os.path.basename(archive_path)
        no_ext = filename.split(".")[0]
        path = "/data/web_static/releases/{}/".format(no_ext)
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(path))
        run('tar -xzf /tmp/{} -C {}'.format(filename, path))
        run('rm /tmp/{}'.format(filename))
        run('mv {}web_static/* {}'.format(path, path))
        run('rm -rf {}web_static'.format(path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(path))
        return True
    except:
        return False


def deploy():
    """
    Create and distribute an archive to the web servers.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
