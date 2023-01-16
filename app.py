from flask import Flask, request

app = Flask(__name__)


# {
#     user_id: int
#     time_type: enum
# }

@app.route('/analytics', methods=['POST'])
def retrieve_rating_analytics():
    user_id = request.json.get('user_id')
    time_type = request.json.get('time_type')
    return {"t": time_type}


if __name__ == '__main__':
    app.run()
