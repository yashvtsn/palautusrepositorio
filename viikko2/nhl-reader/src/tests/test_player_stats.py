import unittest

from player import Player
from player_stats import PlayerStats


class StubPlayerReader:
    def __init__(self, players):
        self.players = players

    def get_players(self):
        return self.players


def make_player(name, team, goals, assists):
    return Player({
        "name": name,
        "nationality": "FIN",
        "assists": assists,
        "goals": goals,
        "team": team,
        "games": 10,
        "id": name
    })


class TestPlayerStats(unittest.TestCase):
    def test_top_scorers_by_team_filters_and_sorts_by_points(self):
        players = [
            make_player("Assist Specialist", "BOS", 2, 9),
            make_player("Goal Scorer", "BOS", 8, 1),
            make_player("Other Team", "TOR", 20, 20),
        ]
        stats = PlayerStats(StubPlayerReader(players))

        result = stats.top_scorers_by_team("BOS")

        self.assertEqual(
            [player.name for player in result],
            ["Assist Specialist", "Goal Scorer"]
        )


if __name__ == "__main__":
    unittest.main()
