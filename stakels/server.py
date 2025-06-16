from flask import Flask, jsonify, request
from .app import BetManager

app = Flask(__name__)
manager = BetManager()

@app.post('/users')
def create_user():
    data = request.get_json()
    username = data.get('username')
    if not username:
        return jsonify({'error': 'username required'}), 400
    user = manager.create_user(username)
    return jsonify({'username': user.username, 'balance': user.balance}), 201

@app.post('/bets')
def create_bet():
    data = request.get_json()
    try:
        bet = manager.create_bet(
            description=data['description'],
            amount=float(data['amount']),
            creator=data['creator'],
            opponent=data['opponent']
        )
    except (KeyError, ValueError) as exc:
        return jsonify({'error': str(exc)}), 400
    return jsonify({'id': bet.id}), 201

@app.get('/bets')
def list_bets():
    bets = [bet.__dict__ for bet in manager.list_bets()]
    return jsonify(bets)

if __name__ == '__main__':
    app.run(debug=True)
