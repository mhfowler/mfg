import io
import random
from uuid import uuid4
from PIL import Image, ImageEnhance, ImageDraw, ImageFont
from urllib import request
from collections import namedtuple

FONT = '/home/ftseng/.fonts/terminal-grotesque.ttf'

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    _chunks = []
    for i in range(0, len(l), n):
        _chunks.append(l[i:i + n])
    return _chunks

def gen_image(urls, text='', mixture_size=(400,250)):
    assert len(urls) >= 3
    random.shuffle(urls)
    mimg = blend_images(urls, target_size=mixture_size)
    mimg = draw_text(text, mimg)
    fname = '{}.jpg'.format(uuid4())
    mimg.save(fname, 'jpeg', quality=0)
    return fname

def draw_text(text, img):
    font = ImageFont.truetype(FONT, 40)
    text = '\n'.join(chunks(text, 22))
    d = ImageDraw.Draw(img)
    d.text((3,3), text, font=font, fill=(0,0,0,255))
    d.text((0,0), text, font=font, fill=(255,255,255,255))
    return img

def download_image(url):
    req = request.Request(url, headers={'User-Agent': 'Chrome'})
    resp = request.urlopen(req)
    data = io.BytesIO(resp.read())
    try:
        return Image.open(data)
    except OSError:
        return None


def resize_image(img, target_size):
    Point = namedtuple('Point', ['x', 'y'])
    size = Point(*img.size)
    target_size = Point(*target_size)

    # Scale as needed
    x_scale = target_size.x/size.x
    y_scale = target_size.y/size.y
    scale_factor = max(x_scale, y_scale)
    scaled_size = Point(*[int(d*scale_factor) for d in size])
    img = img.resize(scaled_size)

    # Crop as needed
    if scaled_size.x == target_size.x:
        l, r = 0, target_size.x
    else:
        x_center = scaled_size.x/2
        l = int(x_center - target_size.x/2)
        r = int(x_center + target_size.x/2)

    if scaled_size.y == target_size.y:
        u, d = 0, target_size.y
    else:
        y_center = scaled_size.y/2
        u = int(y_center - target_size.y/2)
        d = int(y_center + target_size.y/2)

    img = img.crop((l,u,r,d))

    # Sometimes we may be one pixel off,
    # so just adjust if necessary
    if img.size != target_size:
        img = img.resize(target_size)

    return img


def fit_image(img, target_size):
    Point = namedtuple('Point', ['x', 'y'])
    size = Point(*img.size)
    target_size = Point(*target_size)

    # Scale as needed
    x_scale = target_size.x/size.x
    y_scale = target_size.y/size.y
    scale_factor = min(x_scale, y_scale)
    scaled_size = Point(*[int(d*scale_factor) for d in size])
    img = img.resize(scaled_size)

    # Place on background
    back = Image.new('RGBA', target_size, color=1)

    l = int(target_size.x/2 - scaled_size.x/2)
    r = int(target_size.x/2 + scaled_size.x/2)
    u = int(target_size.y/2 - scaled_size.y/2)
    d = int(target_size.y/2 + scaled_size.y/2)
    back.paste(img, (l,u,r,d))

    return back

def blend_images(urls, target_size=(400, 250)):
    """
    Combine two images, then apply a mask onto a transparent background.
    """
    images = []
    for url in urls:
        img = download_image(url)
        # If the image was malformed or something,
        # just make a blank image
        if img is None:
            img = Image.new('RGBA', target_size, color=1)
        img = img.convert('RGBA')
        images.append(img)

    cimages = []
    for img in images:
        img = resize_image(img, target_size)
        bright = ImageEnhance.Brightness(img)
        img = bright.enhance(0.8)
        cimages.append(img)

    the_img = Image.blend(cimages[0], cimages[1], 0.5)
    for img in cimages[2:]:
        the_img = Image.blend(the_img, img, 0.5)
    return the_img