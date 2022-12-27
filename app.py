
from flask import Flask, request, render_template
import pytesseract

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded image
        image = request.files['image']
        # Use pytesseract to extract text from the image
        text = pytesseract.image_to_string(image.filename, config='--psm 3')
        # Render the text in the template
        return render_template('index.html', text=text)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
