import os
from color_matcher import ColorMatcher, __version__
from color_matcher.io_handler import load_img_file, save_img_file
from color_matcher.normalizer import Normalizer

# Paths
frame_input_folder = '/content/color-matcher/MyFolder/Frames'
cframe_output_folder = '/content/color-matcher/MyFolder/ColorMatchFrame'
creference_image_path = '/content/color-matcher/tests/data/scotland_plain.png'

# Load the reference image
img_ref = load_img_file(creference_image_path)

# Instantiate ColorMatcher
cm = ColorMatcher()

# Ensure the output folder exists
os.makedirs(cframe_output_folder, exist_ok=True)

# Process each frame
for frame_name in os.listdir(frame_input_folder):
    if frame_name.endswith('.png'):
        # Load the source image (frame)
        img_src = load_img_file(os.path.join(frame_input_folder, frame_name))

        # Apply color matching
        img_res = cm.transfer(src=img_src, ref=img_ref, method='hm-mvgd-hm')  # "default", "hm", "reinhard", "mvgd", "mkl", "hm-mvgd-hm", "hm-mkl-hm"

        # Normalize image intensity to 8-bit unsigned integer
        img_res = Normalizer(img_res).uint8_norm()

        # Save the color-corrected frame
        output_frame_name = os.path.splitext(frame_name)[0] + '-c.png'
        save_img_file(img_res, os.path.join(cframe_output_folder, output_frame_name))
