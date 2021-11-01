import flask
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

books = [
		{'id': 0,
		 'title': 'A Fire Upon the Deep',
		 'author': 'Vernor Vinge',
		 'first_sentence': 'The coldsleep itself was dreamless.',
		 'year_published': '1992'},
		{'id': 1,
		 'title': 'The Ones Who Walk Away From Omelas',
		 'author': 'Ursula K. Le Guin',
		 'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
		 'published': '1973'},
		{'id': 2,
		 'title': 'Dhalgren',
		 'author': 'Samuel R. Delany',
		 'first_sentence': 'to wound the autumnal city.',
		 'published': '1975'}
]

@app.route('/', methods=['GET'])
def home():
	return "<h1>Distant Reading Archives</h1>"

apispace = '/api/v1/resources'

# A route to all book resources
@app.route(apispace+'/books/all', methods=['GET'])
def book_all():
	return jsonify(books)

# A route to get detail on single book
@app.route(apispace+'/books', methods=['GET'])
def book_id():
	if 'id' in request.args:
		id = int(request.args['id'])
	else:
		return "Error, book id is not specified, please provide id"

	results = []

	for book in books:
			if book['id'] == id:
					results.append(book)

	return jsonify(results)

app.run()
