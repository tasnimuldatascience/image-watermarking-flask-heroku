
# Image Watermarking Flask App

This project is a Flask-based web application that allows users to add watermarks to images. The app provides two watermarking options:
1. **Logo Watermark** - Upload a logo to be placed as a watermark.
2. **Text Watermark** - Add a custom text as a watermark.

## Features
- Upload an image and add a **logo watermark** with adjustable transparency.
- Add a **text watermark** with customizable size and position.
- View and download the watermarked images.
- Deployed on **Heroku** for ease of use.

---

## Project Structure
```
IMAGE WATERMARKING FLASK APP/
├── app/
│   ├── __init__.py
│   ├── views.py
│   ├── static/
│   ├── templates/
│   │   └── index.html
├── images/
│   ├── logo_watermark.png   # Sample logo watermark output
│   ├── text_watermark.png   # Sample text watermark output
├── uploads/                        # Folder to store uploaded images
├── app.py                          # Main Flask app entry point
├── config.py                       # Configuration file for the app
├── requirements.txt                # Python dependencies
├── readme.md                       # Project documentation
```

---

## Sample Outputs

### 1. Logo Watermark Output
![Logo Watermark](images/logo_watermark.png)

### 2. Text Watermark Output
![Text Watermark](images/text_watermark.png)

---

## How to Run Locally
1. Clone the repository:
    ```bash
    git clone https://github.com/tasnimuldatascience/image-watermarking-flask-heroku.git
    cd image-watermarking-flask-app
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask app:
    ```bash
    python app.py
    ```

4. Open the app in your browser at:
    ```
    http://127.0.0.1:5000/
    ```

---

## How to Deploy on Heroku
1. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
2. Log in to your Heroku account:
    ```bash
    heroku login
    ```

3. Create a new Heroku app:
    ```bash
    heroku create your-app-name
    ```

4. Deploy the app:
    ```bash
    git add .
    git commit -m "Initial commit"
    git push heroku main
    ```

5. Open your app in the browser:
    ```bash
    heroku open
    ```

---

## Configuration
Modify the `config.py` file to customize the application settings.
