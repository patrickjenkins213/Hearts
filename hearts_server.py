import argparse
import json

from flask import Flask, request

from hearts import Hearts


class HeartsServer(Flask):
    def __init__(self, import_name):
        super(HeartsServer, self).__init__(import_name)

        self.open_games = {}

        self.add_url_rule('/', 'index', self.hello, methods=["GET"])
        self.add_url_rule('/games', 'games', self.games, methods=["GET"])
        self.add_url_rule('/join', 'join', self.join, methods=["POST"])
        self.add_url_rule('/create_game', 'create_game', self.create_game, methods=["POST"])

    def hello(self):
        return "Hello world!"

    def games(self):
        return json.dumps({"games": list(self.open_games.keys())})

    def join(self):
        data = request.json
        if self.open_games[data["game_id"]].add_player(data["player_id"]):
            return json.dumps({"success": True})
        return json.dumps({"success": False})

    def create_game(self):
        data = request.json
        game = Hearts(data["game_id"])
        self.open_games[game.id] = game
        return json.dumps({"game_id": game.id})


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--port', default=8080)

    return parser.parse_args()


if __name__ == '__main__':
    ARGS = parse_args()
    hs = HeartsServer(__name__)
    hs.run(ARGS.host, ARGS.port)
