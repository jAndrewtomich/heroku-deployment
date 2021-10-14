from app import db


class HackerWars(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    player = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, player, password):
        self.player = player
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)

