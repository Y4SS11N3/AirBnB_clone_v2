from fabric.api import local
from datetime import datetime

def do_pack():
    """Generate a .tgz archive from the contents of the web_static folder."""
    try:
        # Create the versions folder if it doesn't exist
        local("mkdir -p versions")

        # Generate the timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        # Create the archive path
        archive_path = "versions/web_static_{}.tgz".format(timestamp)

        # Create the archive
        local("tar -cvzf {} web_static".format(archive_path))

        return archive_path

    except:
        return None
