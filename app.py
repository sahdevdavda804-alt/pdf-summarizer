from flask import Flask, render_template, request, send_file
from summarizer import summarize_pdf
from utils import create_pdf

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    summary = None

    if request.method == 'POST':

        file = request.files['pdf']

        if file:
            summary = summarize_pdf(file)

    return render_template(
        'index.html',
        summary=summary
    )


@app.route('/download', methods=['POST'])
def download():

    summary = eval(request.form['summary'])

    pdf_path = create_pdf(summary)

    return send_file(
        pdf_path,
        as_attachment=True
    )


if __name__ == '__main__':
    app.run(debug=True)