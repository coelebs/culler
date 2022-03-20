import glob
import os
import exiv2

class RawFolder(object):
    def __init__(self):
        self.folder = "testfolder/"
        self.filelist = [Photo(x) for x in sorted(glob.glob(os.path.join(self.folder, "*.cr2")))]
        self._position = 0

    def get_next_image(self):
        self._position += 1
        return self.get_image()
    
    def get_prev_image(self):
        self._position -= 1
        return self.get_image()

    def get_image(self):
        return self.filelist[self._position]

class Photo(object):
    def __init__(self, path):
        self.path = path
        self.stars = "NO"

    def get_date(self):
        self.image = exiv2.ImageFactory.open(self.path)
        self.image.readMetadata() #read data when needed
        data = self.image.exifData()
        # TODO proper printing of datetime probably
        return str(data['Exif.Image.DateTime']).split(":", maxsplit=1)[1]

    def rate(self, stars):
        self.stars = stars

    def rating(self):
        return self.stars
    
    def __str__(self):
        return self.path
