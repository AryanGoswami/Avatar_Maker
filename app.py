import os
import streamlit as st

from main import Avatar
from part import AvatarPart

log = []

BASE_DIR = os.path.dirname(__file__)
IMAGE_DIR = os.path.join(BASE_DIR, "images")


st.title("Mini Avatar Creator")

avatar = Avatar()

CATEGORIES = ["base", "expression"]

for category in CATEGORIES:
    category_path = os.path.join(IMAGE_DIR, category)
    if not os.path.exists(category_path):
        st.error(f"Folder not found:  {category_path}")
        continue

    options = [f for f in os.listdir(category_path) if f.lower().endswith((".png", ",jpg"))]
    if not options:
        st.warning(f"No images found in {category}")
        continue

    selected = st.selectbox(f"Select {category}", options, key=category)
    image_path = os.path.join(category_path, selected)

    log.append(f"📁 Loaded image '{selected}' from '{category}' folder.")
    log.append(f"🧩 Creating AvatarPart object for '{category}'.")

    part = AvatarPart(selected, image_path)
    avatar.set_part(category, part)

    log.append(f"✅ Assigned '{selected}' to avatar under category '{category}'.")

try:
    final_image = avatar.render()
    st.image(final_image, caption="Your Avatar")

    st.subheader("🧱 Avatar Object Structure")
    st.text(str(avatar))

    st.subheader("🛠️ Process Log")
    st.code("\n".join(log), language="text")
except Exception as e:
    st.error(f"Error rendering avatar: {e}")