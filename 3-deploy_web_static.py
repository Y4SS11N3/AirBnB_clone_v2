#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to web servers
"""
from fabric.api import env, local, put, run, runs_once
from datetime import datetime
import os.path

env.hosts = ['54.90.33.112', '23.23.75.134']


@runs_once
def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static.
    """
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")
        now = datetime.now()
        file_format = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second)
        local("tar -cvzf {} web_static".format(file_format))
        return file_format
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    """
    if not os.path.exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(path, no_ext))
        run("tar -xzf /tmp/{} -C {}{}/".format(file_name, path, no_ext))
        run("rm /tmp/{}".format(file_name))
        run("mv {}{}/web_static/* {}{}/".format(path, no_ext, path, no_ext))
        run("rm -rf {}{}/web_static".format(path, no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, no_ext))
        print("New version deployed!")
        return True
    except Exception as e:
        print(f"Deployment failed: {e}")
        return False


def deploy():
    """
    Full deployment function
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
