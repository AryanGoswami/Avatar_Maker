# CATEGORIES = ["base", "expression"]

from part import AvatarPart
class Avatar:
    def __init__(self):
        self.parts = {}

    def set_part(self, category, part: AvatarPart):
        self.parts[category] = part
    
    def render(self):
        base = self.parts.get("base")
        if not base:
            raise ValueError("Base image is required to render avatar.")
        final = base.image.copy()

        render_order = ['expression']

        for category in render_order:
            part = self.parts.get(category)
            if part:
                final.alpha_composite(part.image)
        return final
    
    def __str__(self):
        output = "Avatar Structure: \n"
        for category, part in self.parts.items():
            output += f" {category}: {part}\n"
        return output