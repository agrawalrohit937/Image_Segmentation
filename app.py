# from flask import Flask, render_template, request, jsonify
# from utils import predict_emotion
# import os

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['GET', 'POST'])
# def predict():
#     if request.method == 'POST':
#         file = request.files.get('file')
#         if file and file.filename != '':
#             img_bytes = file.read()
#             prediction = predict_emotion(img_bytes)
#             return render_template('result.html', prediction=prediction)
#     return render_template('predict.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# # if __name__ == '__main__':
# #     app.run(debug=True)
# # if __name__ == "__main__":
# #     app.run(debug=True, host='0.0.0.0', port=5000)


# if __name__ == "__main__":
#     port = int(os.environ.get('PORT', 5000))  # Use Railway's PORT if available
#     app.run(debug=True, host='0.0.0.0', port=port)

from flask import Flask, render_template, request
from utils import predict_emotion
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and file.filename != '':
            img_bytes = file.read()
            prediction = predict_emotion(img_bytes)
            return render_template('result.html', prediction=prediction)
    return render_template('predict.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
