# Important imports
from app import app
from flask import request, render_template, redirect, url_for
import os
from skimage.metrics import structural_similarity
import imutils
import cv2
import numpy as np
from PIL import Image

# Adding path to config
app.config['INITIAL_FILE_UPLOADS'] = 'app/static/uploads'

# Route to home page
@app.route("/", methods=["GET", "POST"])
def index():
    # Execute if request is GET
    if request.method == "GET":
        return render_template("index.html")

    # Execute if request is POST
    if request.method == "POST":
        option = request.form.get('options')
        image_upload = request.files.get('image_upload')

        if not image_upload:
            return render_template("index.html", error="No image uploaded. Please upload an image.")

        imagename = image_upload.filename

        # Load the base image
        image = Image.open(image_upload)
        image_logow = np.array(image.convert('RGB'))
        h_image, w_image, _ = image_logow.shape

        # Option 1: Logo Watermark
        if option == 'logo_watermark':
            logo_upload = request.files.get('logo_upload')

            if not logo_upload:
                return render_template("index.html", error="No logo uploaded. Please upload a logo for watermarking.")

            logo = Image.open(logo_upload)
            logo = np.array(logo.convert('RGB'))
            h_logo, w_logo, _ = logo.shape

            # Calculate position for center placement
            center_y = int(h_image / 2)
            center_x = int(w_image / 2)
            top_y = center_y - int(h_logo / 2)
            left_x = center_x - int(w_logo / 2)
            bottom_y = top_y + h_logo
            right_x = left_x + w_logo

            # Ensure ROI does not exceed image boundaries
            if top_y < 0 or left_x < 0 or bottom_y > h_image or right_x > w_image:
                return render_template("index.html", error="The logo is too large for the base image.")

            # Add the logo with transparency
            roi = image_logow[top_y:bottom_y, left_x:right_x]
            alpha_logo = 0.3  # Adjust logo transparency
            alpha_image = 1 - alpha_logo
            result = cv2.addWeighted(roi, alpha_image, logo, alpha_logo, 0)

            # Optional: Draw guide lines
            cv2.line(image_logow, (0, center_y), (left_x, center_y), (0, 0, 255), 1)
            cv2.line(image_logow, (right_x, center_y), (w_image, center_y), (0, 0, 255), 1)

            # Replace ROI with the blended logo
            image_logow[top_y:bottom_y, left_x:right_x] = result

            # Save and return the updated image
            img = Image.fromarray(image_logow, 'RGB')
            img.save(os.path.join(app.config['INITIAL_FILE_UPLOADS'], 'image.png'))
            full_filename = 'static/uploads/image.png'
            return render_template('index.html', full_filename=full_filename)

        # Option 2: Text Watermark
        elif option == 'text_watermark':
            text_mark = request.form.get('text_mark', 'Default Watermark')

            # Increase text size and adjust positioning
            cv2.putText(
                image_logow,
                text=text_mark,
                org=(w_image - 300, h_image - 40),  # Adjusted position for better visibility
                fontFace=cv2.FONT_HERSHEY_COMPLEX,
                fontScale=1.5,  # Increased font size
                color=(0, 0, 255),
                thickness=3,  # Increased thickness for better visibility
                lineType=cv2.LINE_AA
            )

            # Save and return the updated image
            timg = Image.fromarray(image_logow, 'RGB')
            timg.save(os.path.join(app.config['INITIAL_FILE_UPLOADS'], 'image1.png'))
            full_filename = 'static/uploads/image1.png'
            return render_template('index.html', full_filename=full_filename)

        else:
            # Handle invalid or no option selected
            return render_template("index.html", error="Please select a valid option.")

# Main function
if __name__ == '__main__':
    app.run(debug=True)