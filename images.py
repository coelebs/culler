import glob
import os

class RawFolder(object):
    def __init__(self):
        self.folder = "testfolder/"
        self.filelist = sorted(glob.glob(os.path.join(self.folder, "*.cr2")))
        self._position = 0

    def get_next_image(self):
        self._position += 1
        return self.get_image()
    
    def get_prev_image(self):
        self._position -= 1
        return self.get_image()

    def get_image(self):
        return self.filelist[self._position]
