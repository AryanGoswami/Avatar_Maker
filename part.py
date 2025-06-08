from PIL import Image
class AvatarPart:
    def __init__(self, name, img_path):
        self.name = name
        self.img_path = img_path
        self.image = Image.open(img_path).convert("RGBA")

    def __str__(self):
        return f"{self.name}"