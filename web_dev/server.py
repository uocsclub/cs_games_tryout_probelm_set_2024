from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

books = [
    {
        'id': 1,
        'publish': '2024-02-10',
        'title': 'The Journey of Wisdom',
        'author': 'John Doe',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed et suscipit nunc, eget consequat libero. Phasellus vel ullamcorper mauris, at gravida purus. Integer consequat, turpis nec accumsan ullamcorper, odio ante placerat elit, vitae consectetur justo neque a risus. Aliquam erat volutpat. Suspendisse potenti. Donec vel velit sem. Nulla facilisi.'
    },
    {
        'id': 2,
        'publish': '2021-12-12',
        'title': 'Echoes of Eternity',
        'author': 'Jane Smith',
        'content': 'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Fusce pretium pharetra libero eget viverra. Vivamus rhoncus, velit in fermentum faucibus, mi velit interdum enim, nec consequat ligula turpis id velit. Integer sed sapien erat. Nam aliquam efficitur magna, nec viverra est cursus ac.'
    },
    {
        'id': 3,
        'publish': '2023-05-20',
        'title': 'Secrets Unveiled',
        'author': 'Emily Johnson',
        'content': 'Suspendisse potenti. In hac habitasse platea dictumst. Morbi congue auctor dui, sed tincidunt justo fringilla nec. Fusce sit amet odio id velit suscipit fermentum. Vestibulum eleifend, leo a convallis luctus, sapien lorem vestibulum quam, et rutrum lorem urna vel justo.'
    },
    {
        'id': 4,
        'publish': '2022-09-15',
        'title': 'A Tale of Shadows',
        'author': 'Michael Brown',
        'content': 'Vestibulum sodales justo ligula, vel aliquet quam gravida a. Nulla facilisi. Integer elementum eros non nulla bibendum, ac vehicula odio efficitur. Quisque nec mauris eu nunc malesuada dapibus. In non nulla fermentum, vehicula nibh ut, bibendum dui. Mauris sagittis tincidunt arcu id euismod. In hac habitasse platea dictumst.'
    },
    {
        'id': 5,
        'publish': '2020-07-08',
        'title': 'Whispers in the Wind',
        'author': 'David Wilson',
        'content': 'Cras ullamcorper eget nisi at consequat. Nullam vitae hendrerit ex. Sed vestibulum mauris ut dapibus ultricies. Mauris ut nulla et tortor fringilla interdum. Curabitur a risus non libero faucibus lacinia. Nullam quis efficitur mauris. Suspendisse potenti. Fusce ut est luctus, iaculis magna eu, lacinia elit.'
    },
    {
        'id': 6,
        'publish': '2023-10-25',
        'title': 'Lost in Reflection',
        'author': 'Sarah Taylor',
        'content': 'Aliquam erat volutpat. Ut volutpat rutrum libero, vel aliquet arcu consequat nec. Vivamus id enim sit amet lacus posuere iaculis. Suspendisse vel odio et odio aliquam dapibus. Proin malesuada arcu eget fermentum vehicula. In nec odio nisi. Cras id nunc hendrerit, volutpat velit at, efficitur nisl.'
    }
]

highlight_text = {
    1: [{
        "range": (10, 30),
        "comment": "Captivating introduction"
    }],
    2: [{
        "range": (50, 80),
        "comment": "Intriguing plot twist"
    }],
    3: [{
        "range": (20, 45),
        "comment": "Emotional climax"
    }],
    4: [{
        "range": (5, 25),
        "comment": "Suspenseful build-up"
    }],
    5: [{
        "range": (40, 60),
        "comment": "Heartwarming resolution"
    }],
    6: [{
        "range": (15, 35),
        "comment": "Unexpected revelation"
    }]
}

# Homepage route to get list of books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Book page route to get details of a specific book
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404
    
# Route to handle text highlighting and editing comments
@app.route('/books/<int:book_id>/highlight', methods=['GET'])
def get_highlight_text(book_id):
    if not int(book_id) in highlight_text:
        return jsonify({'message': 'Book not found'}), 404
    
    data = highlight_text[book_id]

    return jsonify(data)

@app.route('/books/<int:book_id>/highlight/append', methods=['POST'])
def append_highlight_text(book_id):
    if not book_id in highlight_text:
        return jsonify({'message': 'Book not found'}), 404
    
    
    data = highlight_text[book_id]
    
    range = (int(request.args.get('range_start')), int(request.args.get('range_end')))
    comment = request.args.get('comment')

    data = highlight_text[book_id]
    
    data.append({"range": range, "comment": comment})
    return jsonify(data), 200

# Route to handle text filtering
@app.route('/books/filter', methods=['GET'])
def filter_books():
    keyword = request.args.get('keyword')
    keyword = keyword.lower()
    filtered_books = [
        book for book in books if
        keyword in book['content'].lower() or
        keyword in book['author'].lower() or
        keyword in book['title'].lower()
    ]
    return jsonify(filtered_books)

if __name__ == '__main__':
    app.run(debug=True)
