import json
import os
import yaml

from pytest_test_marker.exceptions import IncompatibleFileType


content_loaders = {'.yml': yaml.safe_load,
                   '.yaml': yaml.safe_load,
                   '.json': json.load}


def get_loader_for_file(extension):
    return content_loaders[extension]


class ManifestFile(object):

    def __init__(self, filename):
        self.fd = open(filename, 'r')
        self._ext = os.path.splitext(filename)[1]

        exts = content_loaders.keys()
        if self._ext not in content_loaders.keys():
            raise IncompatibleFileType("""Please use a manifest file with a
                                       supported extension: {}""".format(exts))

    def __del__(self):
        self.fd.close()

    def get_marks(self):
        return get_loader_for_file(self._ext)(self.fd)
