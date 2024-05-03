#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir

env.hosts = ['54.90.33.112', '23.23.75.134']


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static.
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception:
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
        # Upload the archive to the /tmp/ directory of the web server
        with hide('running'):
            put(archive_path, '/tmp/')

        # Get the filename without extension
        filename = archive_path.split('/')[-1].split('.')[0]

        # Uncompress the archive to the releases folder
        with hide('running'):
            run('mkdir -p /data/web_static/releases/{}/'.format(filename))
            run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'.format(
                filename, filename))

        # Remove the archive from the web server
        with hide('running'):
            run('rm /tmp/{}.tgz'.format(filename))

        # Move the contents of the web_static folder one level up
        with hide('running'):
            run('mv /data/web_static/releases/{}/web_static/* '
                '/data/web_static/releases/{}/'.format(filename, filename))
            run('rm -rf /data/web_static/releases/{}/web_static'.format(
                filename))

        # Remove the current symlink
        with hide('running'):
            run('rm -rf /data/web_static/current')

        # Create a new symlink pointing to the new release
        with hide('running'):
            run('ln -s /data/web_static/releases/{}/ '
                '/data/web_static/current'.format(filename))

        print("New version deployed!")
        return True

    except Exception:
        return False


def deploy():
    """
    Creates and distributes an archive to the web servers.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
