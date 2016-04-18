"""High-level instructions for playing a round of Hanabi.

Intended to be imported into a wrapper (hanabi_wrapper) so that more than one
round can be played.  Low-level details, along with thorough documentation, are
in another module (hanabi_classes).
"""

from hanabi_classes import *

def play_one_round(gameType, players, names, verbosity, deck=None):
    """Play a full round and return the score (int)."""
    r = Round(gameType, names, verbosity, deck) # Instance of a single Hanabi round
    r.deal_hands()

    while r.gameOverTimer != 0:

        if all(x == max(SUIT_CONTENTS) for x in r.progress.values()):
            break # End round early if already won.

        if r.lightning == N_LIGHTNING:
            return 0 # Award no points for a loss.  TODO: togglable behavior?

        r.ai_play(players[r.whoseTurn]) # Play one turn.

    return sum(r.progress.values()) # Final score

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

    def player_types():
        return [playerInfo[0] for playerInfo in self.playerInfo]

    def player_names():
        return [playerInfo[1] for playerInfo in self.playerInfo]

    def player_instances():
        return [playerInfo[2] for playerInfo in self.playerInfo]

    def start(self):
        self.round = Round(self.gameType, self.player_names(), self.verbosity, self.deck)
        self.deal_hands()

    def reset(self):
        self.round = None

    def game_started(self):
        if not self.round:
            return False
        return self.round.turnNumber != 0

    def game_over(self):
        if not self.round:
            return False
        return self.round.gameOverTimer == 0

    def next(self):
        if not self.round:
            self.start()

        pInstances = self.playerInstances()
        self.round.get_play(pInstances[self.round.whoseTurn])

    def prev(self):
        # unimplemented
        return

    def save(self):
        # unimplemented
        return

    def load(self):
        # unimplemented
        return
