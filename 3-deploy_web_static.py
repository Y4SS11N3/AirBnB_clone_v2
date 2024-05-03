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
    """Archive the static files"""
    try:
        datetime_obj = datetime.now().strftime("%Y%m%d%H%M%S")
        file_path = "versions/web_static_{}.tgz".format(datetime_obj)
        if os.path.isdir("versions") is False:
            local("mkdir versions")
        local("tar -cvzf {} web_static".format(file_path))
        return file_path
    except Exception as e:
        print(f"Error: {e}")
        return None


def do_deploy(archive_path):
    """
    Deploys the static files to the webservers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        file_name = os.path.basename(archive_path)
        folder_path = file_name.strip(".tgz")
        run("mkdir -p /data/web_static/releases/{}/".format(folder_path))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            file_name, folder_path))
        run("rm /tmp/{}".format(file_name))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(
                folder_path, folder_path))
        run("rm -rf /data/web_static/releases/{}/web_static".format(
            folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} /data/web_static/current"
            .format(folder_path))
        print("New version deployed!")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def deploy():
    """
    Full deployment function
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
