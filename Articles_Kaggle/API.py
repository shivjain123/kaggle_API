import flask
import csv

with open('shared_articles.csv', newline = '', encoding='utf8') as f:
    reader = list(csv.reader(f))
    all_articles = reader[1:]

app = flask.Flask(__name__)

liked = []
dis_liked = []

@app.route('/all-articles')
def getAllArticles():
    return flask.jsonify({
        'data': all_articles,
        'message': 'success'
    })

@app.route('/liked-art', methods = ["POST"])
def likedArticles():
    article = all_articles[0]
    liked.append(article)
    all_articles.pop(0)
    print(liked)
    return flask.jsonify({
        'status': 'success'
    }), 200

@app.route('/disliked-art', methods = ["POST"])
def dislikedArticles():
    article = all_articles[0]
    dis_liked.append(article)
    all_articles.pop(0)
    return flask.jsonify({
        'status': 'success'
    }), 200

if __name__ == '__main__':
    app.run(debug=True)