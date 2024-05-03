#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack, and then
distributes it to your web servers, using the function do_deploy.
"""

from fabric.api import local, put, run, env
from datetime import datetime
import os

env.hosts = ['54.90.33.112', '23.23.75.134']

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
        print("Packing web_static to {}".format(file_format))
        local("tar -cvzf {} web_static".format(file_format))
        file_size = os.path.getsize(file_format)
        print("web_static packed: {} -> {}Bytes".format(file_format, file_size))
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
        run("rsync -av {}{}/web_static/ {}{}/".format(path, no_ext, path, no_ext))
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
    Creates and distributes an archive to the web servers.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    results = []
    for host in env.hosts:
        result = do_deploy(archive_path)
        results.append(result)
    return all(results)

if __name__ == "__main__":
    deploy()
