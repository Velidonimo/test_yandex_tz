import cv2
import requests
import os


class ImagesCompare:
    EVEN = "even"
    UNEVEN = "uneven"
    ERROR = "error"

    def download_image(self, url, name):
        """Downloads the file.
        :param: url: url to download
        :param: name: name for file. Without extension. String.
        :return: True if download was successful or False if not
        """
        name = os.path.join(os.path.dirname(__file__), f'../images/{name}.jpg')
        try:
            r = requests.get(url)
            with open(name, 'wb') as outfile:
                outfile.write(r.content)
        except Exception as e:
            print(e)
            return False
        return True

    def images_are_even(self, name1, name2):
        """Compares two downloaded pictures
            :return:
                ImagesCompare.EVEN if even,
                ImagesCompare.UNEVEN if uneven,
                ImagesCompare.ERROR if can't compare
        """
        name1 = os.path.join(os.path.dirname(__file__), f'../images/{name1}.jpg')
        name2 = os.path.join(os.path.dirname(__file__), f'../images/{name2}.jpg')
        try:
            img1 = cv2.imread(name1)
            img2 = cv2.imread(name2)
            shape1 = img1.shape
            shape2 = img2.shape
        except:
            return self.ERROR

        # check the shape
        if shape1 != shape2:
            return self.UNEVEN

        # subtract images
        delta_img = cv2.absdiff(img1, img2)

        # check all channels of the difference to be 0
        b, g, r = cv2.split(delta_img)
        if any(cv2.countNonZero(x) for x in (b, g, r)):
            return self.UNEVEN
        return self.EVEN

    def delete_images(self, names):
        """Deletes the specified images if they exist
        :param: names = iterable object of image names to delete
        """
        for name in names:
            try:
                os.remove(os.path.join(os.path.dirname(__file__), f'../images/{name}.jpg'))
            except:
                continue


if __name__ == '__main__':
    im = ImagesCompare()
    print(im.images_are_even('img_first', 'img_forw'))
