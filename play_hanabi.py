"""High-level instructions for playing a round of Hanabi.

Intended to be imported into a wrapper (hanabi_wrapper) so that more than one
round can be played.  Low-level details, along with thorough documentation, are
in another module (hanabi_classes).
"""

from hanabi_classes import *

def play_one_round(gameType, playerInfo, verbosity, deck=None):
    """Play a full round and return the score (int)."""
    g = HanabiGame(gameType, playerInfo, verbosity, deck)
    g.start()

    while not g.game_over():

        g.next() # Play one turn.

    return sum(g.round.progress.values()) # Final score

class HanabiGame:
    """Manage a game of Hanabi. Primarily allow the capability to initialize, step
    through (and backward), and save/restore game states interactively. Of course,
    you can also just use it to play a randomized game with the desired logging
    level.
    """

    def __init__(self, gameType="vanilla", playerInfo=(), verbosity="silent", deck=None):

        # For now, just save the argument information
        self.gameType = gameType
        self.playerInfo = playerInfo
        self.verbosity = verbosity
        self.deck = deck

    def player_types(self):
        return [playerInfo[0] for playerInfo in self.playerInfo]

    def player_names(self):
        return [playerInfo[1] for playerInfo in self.playerInfo]

    def player_instances(self):
        return [playerInfo[2] for playerInfo in self.playerInfo]

    def start(self):
        self.round = Round(self.gameType, self.player_names(), self.verbosity, self.deck)
        self.round.deal_hands()

    def reset(self):
        self.round = None

    def game_started(self):
        if not self.round:
            return False
        return self.round.turnNumber != 0

    def game_over(self):
        if not self.round:
            return False

        if self.round.gameOverTimer == 0:
            return True

    def next(self):
        if not self.round:
            self.start()

        pInstances = self.player_instances()
        self.round.ai_play(pInstances[self.round.whoseTurn])

    def prev(self):
        # unimplemented
        return

    def save(self):
        # unimplemented
        return

    def load(self):
        # unimplemented
        return
