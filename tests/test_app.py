from stakels.app import BetManager


def test_create_user_and_bet():
    manager = BetManager()
    alice = manager.create_user('alice')
    bob = manager.create_user('bob')
    bet = manager.create_bet('Winner takes all', 10, 'alice', 'bob')

    assert bet.creator == 'alice'
    assert bet.opponent == 'bob'
    assert bet.amount == 10
    assert bet.id in manager.bets
    assert alice.username == 'alice'
    assert bob.username == 'bob'
