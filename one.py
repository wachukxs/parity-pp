import enum
import random


# models
# colors, player, machine, money

# should have a list of all possible colors there is.
class Color(enum.Enum):
    WHITE = 1
    BLACK = 2
    GREEN = 3
    YELLOW = 4


class Player:
    def __init__(self, name, no_of_plays, money):
        self.name = name
        self.no_of_plays = no_of_plays
        self.money = money

    def play(self):
        print("A single play")


    def receive_money(self, received_amount):
        # if the machine is paying out money, the player should be able to receive it.
        self.money += received_amount
        print(f"Player {self.name} receeved {self.received_amount}")


class Money:
    def __init__(self, amount):
        self.amount = amount  # this is an initial sum of money that the machine has. a float


# take in Money
class Machine:
    def __init__(self, money, cost_of_single_play):
        self.float = money.amount  # adding a "float" to our fruit machine, this is an initial sum of money that the machine has
        self.cost_of_single_play = cost_of_single_play
        self.slots = [Color.BLACK, Color.WHITE, Color.GREEN, Color.YELLOW]
        # create four random colors. or randomize them during play

    def generate_random_colors(self):  # logic to generate random slots
        print("Randomizing slots values")
        for index, slot in enumerate(self.slots):
            self.slots[index] = Color(random.randint(1, len(self.slots)))

    def determine_game_won(self, player) -> bool:  # our esteemed prize system
        print("Checking if game has been won")
        # checking: If each slot has a different colour
        # then the machine should pay out half the current money in the machine.
        # create a set from our list of slot and compare length
        if len(set(self.slots)) == len(self.slots):
            print("Each slot has a different color. Paying our half the current money we have.")
            player.money.amount += self.float // 2  # returning integer cause we're running a business here
            return True
        elif len(self.check_for_duplicates()) > 0 and self.check_for_adjacents_in_slot():
            # two (or more) adjacent slots with same colour, paying out (5 x single play).
            print("There are adjacent duplicates")
            if self.float > (5 * self.cost_of_single_play):
                player.money.amount += 5 * self.cost_of_single_play
            else:
                self.insufficient_prize_for_player(player)
            return True
        return False

    def insufficient_prize_for_player(self, player):
        player.no_of_plays += (5 * self.cost_of_single_play) - self.float

    def check_for_duplicates(self):
        duplicates = []
        for color in self.slots:
            _count = self.slots.count(color)
            if _count > 1:
                duplicates.append(color)
        return duplicates

    def check_for_adjacents_in_slot(self):
        print("checking for adjacents")
        # if any(self.slots.count(_color) > 1 for _color in self.slots):
        if len(self.check_for_duplicates()) > 0:
            for duplicate_color in self.check_for_duplicates():
                adjacent_index = self.slots.index(duplicate_color) + 1
                if self.slots[adjacent_index].name == duplicate_color.name:
                    print("Found duplicates")
                    return True
        return False

    def play(self, player):
        # Each time a player plays our fruit machine
        # we display four 'slots' each with a randomly selected colour in each slot.
        self.generate_random_colors()
        print(f"Play no. {player.no_of_plays} from player {player.name}")
        player.no_of_plays -= 1
        self.determine_game_won(player)


# running our code
player1 = Player("Gary", 5, Money(4))

machine = Machine(Money(45), 5)
machine.play(player1)
