from hello_utilities.log_helper import _log
from google import google, images
from hello_settings import PROJECT_PATH
import os


TEMP_PATH = os.path.join(PROJECT_PATH, 'temp')


def printer1(question):
    print question
    # TODO: make this do a google image search and do something intereting with the results
    # options = images.ImageOptions()
    # options.image_type = images.ImageType.CLIPART
    # options.larger_than = images.LargerThan.MP_4
    # options.color = "green"
    # image_results = google.search_images("banana", options)
    # images.download(image_results, path=TEMP_PATH)
    print question


if __name__ == '__main__':
    printer1('what banana is this?')