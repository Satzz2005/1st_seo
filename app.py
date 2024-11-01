from flask import Flask, render_template, request
from seo3 import HybridSEOSystem  # Adjust this import if necessary

app = Flask(__name__)
hybrid_seo = HybridSEOSystem()

@app.route('/', methods=['GET', 'POST'])
def home():
    results = []
    if request.method == 'POST':
        keyword = request.form['keywords']  # Make sure this matches the input name in your HTML
        # Fetch and analyze based on keyword
        results = hybrid_seo.search_webpages(keyword)  # This should fetch search results based on the keyword
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
