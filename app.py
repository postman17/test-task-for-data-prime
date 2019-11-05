from flask import Flask, request, render_template

from parser import Parser

app = Flask(__name__, template_folder='templates')


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/search", methods=['POST'])
def search():
    url = request.form['url']
    page_num = request.form['page-num']
    main_tag = request.form['main-tag-list']
    tag_class = request.form['main-tag-list-class']
    main_tag_article = request.form['main-tag-article']
    main_tag_article_class = request.form['main-tag-article-class']
    parser = Parser(url, page_num, main_tag, tag_class, main_tag_article, main_tag_article_class)
    data = {'data': parser.clean_data}
    return render_template('result.html', data=data)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
