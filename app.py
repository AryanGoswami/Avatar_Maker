# import os
# import streamlit as st

# from main import Avatar
# from part import AvatarPart

# log = []

# BASE_DIR = os.path.dirname(__file__)
# IMAGE_DIR = os.path.join(BASE_DIR, "images")


# st.title("Mini Avatar Creator")

# avatar = Avatar()

# CATEGORIES = ["base", "expression"]

# for category in CATEGORIES:
#     category_path = os.path.join(IMAGE_DIR, category)
#     if not os.path.exists(category_path):
#         st.error(f"Folder not found:  {category_path}")
#         continue

#     options = [f for f in os.listdir(category_path) if f.lower().endswith((".png", ",jpg"))]
#     if not options:
#         st.warning(f"No images found in {category}")
#         continue

#     selected = st.selectbox(f"Select {category}", options, key=category)
#     image_path = os.path.join(category_path, selected)

#     log.append(f"📁 Loaded image '{selected}' from '{category}' folder.")
#     log.append(f"🧩 Creating AvatarPart object for '{category}'.")

#     part = AvatarPart(selected, image_path)
#     avatar.set_part(category, part)

#     log.append(f"✅ Assigned '{selected}' to avatar under category '{category}'.")

# try:
#     final_image = avatar.render()
#     st.image(final_image, caption="Your Avatar")

#     st.subheader("🧱 Avatar Object Structure")
#     st.text(str(avatar))

#     st.subheader("🛠️ Process Log")
#     st.code("\n".join(log), language="text")
# except Exception as e:
#     st.error(f"Error rendering avatar: {e}")



# import os
# import streamlit as st
# from streamlit_image_select import image_select
# from main import Avatar
# from part import AvatarPart

# # Config
# st.set_page_config(layout="wide")
# st.title("🎨 Mini Avatar Creator with Image Tiles")

# # Paths
# BASE_DIR = os.path.dirname(__file__)
# IMAGE_DIR = os.path.join(BASE_DIR, "images")
# CATEGORIES = ["base", "expression"]

# # Session state
# if "avatar_parts" not in st.session_state:
#     st.session_state.avatar_parts = {}

# avatar = Avatar()
# log = []

# # Process categories
# for category in CATEGORIES:
#     category_path = os.path.join(IMAGE_DIR, category)
#     if not os.path.exists(category_path):
#         st.error(f"❌ Folder not found: {category_path}")
#         continue

#     images = [f for f in os.listdir(category_path) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
#     image_paths = [os.path.join(category_path, f) for f in images]

#     st.markdown(f"### {category.capitalize()}")

#     if images:
#         selected_path = image_select(label=f"Choose a {category}", images=image_paths, use_container_width=False)
#         if selected_path:
#             filename = os.path.basename(selected_path)
#             st.session_state.avatar_parts[category] = AvatarPart(filename, selected_path)
#             log.append(f"✅ Selected {filename} for {category}")
#     else:
#         st.warning(f"No images found for {category}.")

# # Render final avatar
# if all(cat in st.session_state.avatar_parts for cat in CATEGORIES):
#     try:
#         for cat in CATEGORIES:
#             avatar.set_part(cat, st.session_state.avatar_parts[cat])
#         final_image = avatar.render()
#         st.image(final_image, caption="🖼️ Your Avatar", use_column_width=True)
#     except Exception as e:
#         st.error(f"Error rendering avatar: {e}")
# else:
#     st.info("Please select both base and expression images.")

# # Log
# st.subheader("🛠️ Log")
# st.code("\n".join(log) if log else "Nothing selected yet.")



# import os
# import streamlit as st
# from io import BytesIO
# from main import Avatar
# from part import AvatarPart

# # Streamlit Config
# st.set_page_config(layout="wide")
# st.title("🎨 Mini Avatar Creator")

# # Global CSS
# st.markdown("""
#     <style>
# [data-testid="stVerticalBlock"] > div:nth-child(1) {
#     border: 1px solid #444;
#     border-radius: 10px;
#     padding: 10px 15px;
#     background-color: #1e1e1e;
#     transition: box-shadow 0.3s ease, border-color 0.3s ease;
# }

# /* Repeat for other columns */
# [data-testid="stVerticalBlock"] > div:nth-child(2) {
#     border: 1px solid #444;
#     border-radius: 10px;
#     padding: 10px 15px;
#     background-color: #1e1e1e;
#     transition: box-shadow 0.3s ease, border-color 0.3s ease;
# }

# [data-testid="stVerticalBlock"] > div:nth-child(3) {
#     border: 1px solid #444;
#     border-radius: 10px;
#     padding: 10px 15px;
#     background-color: #1e1e1e;
#     transition: box-shadow 0.3s ease, border-color 0.3s ease;
# }

# [data-testid="stVerticalBlock"] > div:nth-child(3):hover {
#     box-shadow: 0 0 2px 2px #ffffff;
#     border-color: #ffffff;
# }
#     </style>
# """, unsafe_allow_html=True)

# # Avatar State
# if "avatar_parts" not in st.session_state:
#     st.session_state.avatar_parts = {}

# BASE_DIR = os.path.dirname(__file__)
# IMAGE_DIR = os.path.join(BASE_DIR, "images")
# CATEGORIES = ["base", "expression"]
# log = []

# def select_image_vertical(category, image_dir):
#     options = [f for f in os.listdir(image_dir) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
#     selected = None
#     for option in options:
#         img_path = os.path.join(image_dir, option)
#         st.image(img_path, width=100)
#         if st.button(f"{category}: {option}", key=f"{category}_{option}"):
#             selected = option
#     return selected

# # Layout
# left_col, center_col, right_col = st.columns([1, 2, 1])

# with left_col:
#     st.subheader("🧱 Base")
#     base_path = os.path.join(IMAGE_DIR, "base")
#     if os.path.exists(base_path):
#         selected = select_image_vertical("base", base_path)
#         if selected:
#             image_path = os.path.join(base_path, selected)
#             st.session_state.avatar_parts["base"] = AvatarPart(selected, image_path)
#             log.append(f"✅ Selected base: {selected}")
#     else:
#         st.error("No base images found.")

# with right_col:
#     st.subheader("😊 Expression")
#     expr_path = os.path.join(IMAGE_DIR, "expression")
#     if os.path.exists(expr_path):
#         selected = select_image_vertical("expression", expr_path)
#         if selected:
#             image_path = os.path.join(expr_path, selected)
#             st.session_state.avatar_parts["expression"] = AvatarPart(selected, image_path)
#             log.append(f"✅ Selected expression: {selected}")
#     else:
#         st.error("No expression images found.")

# with center_col:
#     col1, col2 = st.columns([3, 1])
#     with col1:
#         st.subheader("🖼️ Final Avatar")
#     with col2:
#         if all(cat in st.session_state.avatar_parts for cat in CATEGORIES):
#             avatar = Avatar()
#             for cat, part in st.session_state.avatar_parts.items():
#                 avatar.set_part(cat, part)
#             try:
#                 final_image = avatar.render()
#                 buf = BytesIO()
#                 final_image.save(buf, format="PNG")
#                 buf.seek(0)
#                 st.download_button("⬇️", buf, file_name="avatar.png", mime="image/png", key="download_button")
#             except Exception as e:
#                 st.error(f"Error rendering avatar: {e}")

#     if all(cat in st.session_state.avatar_parts for cat in CATEGORIES):
#         st.image(buf, caption="Your Avatar")
#     else:
#         st.info("Please select both base and expression images.")
#         st.markdown("</div>", unsafe_allow_html=True)

# st.subheader("🛠️ Process Log")
# st.code("\n".join(log), language="text")





import os
from io import BytesIO
import streamlit as st
from streamlit_image_select import image_select
from main import Avatar
from part import AvatarPart

# Streamlit Config
st.set_page_config(layout="wide")
st.title("Mini Avatar Creator")

# Global CSS (optional styling, can remove if you want default look)
# st.markdown("""
#     <style>
# [data-testid="stVerticalBlock"] > div {
#     border: 1px solid #444;
#     border-radius: 10px;
#     padding: 10px 15px;
#     background-color: #1e1e1e;
#     transition: box-shadow 0.3s ease, border-color 0.3s ease;
# }
# [data-testid="stVerticalBlock"] > div:hover {
#     box-shadow: 0 0 2px 2px #ffffff;
#     border-color: #ffffff;
# }
#     </style>
# """, unsafe_allow_html=True)

# Avatar State
if "avatar_parts" not in st.session_state:
    st.session_state.avatar_parts = {}

BASE_DIR = os.path.dirname(__file__)
IMAGE_DIR = os.path.join(BASE_DIR, "images")
CATEGORIES = ["base", "expression"]
log = []

# Layout columns
left_col, center_col, right_col = st.columns([1.2, 1.6, 1.2])

def render_category(category, container):
    category_path = os.path.join(IMAGE_DIR, category)
    if not os.path.exists(category_path):
        container.error(f"No folder found for '{category}'")
        return

    images = [f for f in os.listdir(category_path) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    image_paths = [os.path.join(category_path, img) for img in images]

    if not images:
        container.warning(f"No images in '{category}' folder.")
        return

    selected_path = image_select(label=f"", images=image_paths, use_container_width=False, key=category)
    if selected_path:
        filename = os.path.basename(selected_path)
        st.session_state.avatar_parts[category] = AvatarPart(filename, selected_path)
        log.append(f"✅ Selected {filename} for {category}")

# Left column: base selection
with left_col:
    st.subheader("Base")
    render_category("base", st)

# Right column: expression selection
with right_col:
    st.subheader("Expression")
    render_category("expression", st)

# Center column: render avatar
with center_col:
    col1, col2 = st.columns([6.6, 1.4])
    with col1:
        st.subheader("Final Avatar")
    with col2:
        if all(cat in st.session_state.avatar_parts for cat in CATEGORIES):
            avatar = Avatar()
            for cat, part in st.session_state.avatar_parts.items():
                avatar.set_part(cat, part)
            try:
                final_image = avatar.render()
                buf = BytesIO()
                final_image.save(buf, format="PNG")
                buf.seek(0)
                st.download_button("⬇️", buf, file_name="avatar.png", mime="image/png", key="download_button")
            except Exception as e:
                st.error(f"Error rendering avatar: {e}")

    if all(cat in st.session_state.avatar_parts for cat in CATEGORIES):
        st.image(final_image, caption="Your Avatar")
    else:
        st.info("Please select both base and expression images.")

# Log
st.subheader("🛠️ Process Log")
st.code("\n".join(log) if log else "Nothing selected yet.", language="text")