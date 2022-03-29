import glob
import os
import exiv2

import libxmp

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
        self.xmp = Xmp(self.path)

    def get_date(self):
        self.image = exiv2.ImageFactory.open(self.path)
        self.image.readMetadata() #read data when needed
        data = self.image.exifData()
        # TODO proper printing of datetime probably
        return str(data['Exif.Image.DateTime']).split(":", maxsplit=1)[1]

    def rate(self, stars):
        self.xmp.add_rating(stars)

    def rating(self):
        return self.xmp.get_rating()
    
    def __str__(self):
        return self.path

class Xmp(object):
    def __init__(self, image_path):
        self.path = "%s.xmp" % image_path
        self.xmp = libxmp.XMPMeta()
        try:
            with open(self.path, 'r') as f:
                self.xmp.parse_from_str(f.read())
        except:
            print("proberen")

    def add_rating(self, rating):
        self.xmp.set_property(libxmp.consts.XMP_NS_XMP, "Rating", rating)
        self.write()

    def get_rating(self):
        try:
            return self.xmp.get_property(libxmp.consts.XMP_NS_XMP, "Rating")
        except libxmp.XMPError:
            return "0"

    def write(self):
        with open(self.path, 'w') as f:
            f.write(self.xmp.serialize_to_str(omit_packet_wrapper=True))
