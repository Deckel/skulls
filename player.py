class Player:
    def __init__(self, name, emoji, chips, score) -> None:
        self.name = name
        self.emoji = emoji
        self.chips = chips 
        self.score = score 
        self.live_chips = {}

        self.current_bid = 0

    def __repr__(self) -> str:
        return f"Player {self.emoji}"

    def play_chip(self) -> None:
        move = int(input(f"{self.name} {self.emoji} please add a chip {self.chips}: "))
        # add to live chips
        self.live_chips.update({len(self.live_chips) + 1: self.chips[move]})
        # remove from chips
        self.chips.pop(move)
        # reindex chips
        self.chips = dict(
            zip(
                range(1, len(self.chips) + 1), 
                self.chips.values()
            )
        )