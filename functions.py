import qrcode
from pathlib import Path

def generate(url):
    img = qrcode.make(url)
    BASE_DIR = Path(__file__).resolve().parent
    name = create_slug(10)
    img_path = F"/tmp/{name}.png"
    img.save(img_path)
    return img_path

def create_slug(slug_size):
    letters = string.ascii_letters
    slug_ = ''.join(random.choice(letters) for i in range(slug_size))
    return slug_

