import random

from modifier import Modifier


BOARDS = ['A', 'B', 'C', 'D', 'E', 'F']


class Board(Modifier):

    def __init__(self, number_of_players, thematic, archipelagos, extra_board):
        """
        A board setup for the given number of players

        :param number_of_players: How many Spirits will be played
        :param thematic: Boolean to use thematic board
        :param archipelagos: Boolean to use archipelagos islands
        :param extra_board: Boolean to use an extra board
        """
        if number_of_players == 6 and extra_board:
            assert "Cannot have 6 players and an extra board"

        self.number_of_players = number_of_players
        self.thematic = thematic
        self.archipelagos = archipelagos
        self.extra_board = extra_board
        self.board_list = []
        self.archipelagos_setup = None

        num_of_boards = self.number_of_players
        if self.extra_board:
            num_of_boards += 1
        self._generate_board_list(num_of_boards)

        # Set difficulty
        difficulty = 0
        if self.thematic:
            difficulty += 1
        if self.archipelagos:
            difficulty += 1

        # Add difficulty notes
        harder_notes = []
        if num_of_boards <= 4:
            if 'E' in self.board_list and 'B' in self.board_list:
                harder_notes.append("Boards 'B' and 'E' paired concentrates terrain which can cause swinginess.")
            if 'D' in self.board_list and 'F' in self.board_list:
                harder_notes.append("Boards 'F' and 'D' paired concentrates terrain which can cause swinginess.")
        if self.archipelagos:
            self._archipelagos_setup()
            harder_notes.append('When paired with Scenarios that require gathering many Dahan.')
            harder_notes.append('When paired with Adversaries that focus their forces.')

        super().__init__(difficulty=difficulty, harder_notes=harder_notes)

    def print(self):
        print_message = f'Board Thematic: {self.thematic}, Archipelagos: {self.archipelagos}, Extra Board: ' \
            f'{self.extra_board}, Board List: {self.board_list}'
        if self.archipelagos_setup:
            print_message = f'{print_message} Island Setup: {self.archipelagos_setup}'
        print(print_message)

    def _generate_board_list(self, num_of_boards):
        """
        Generates a list of random boards to use by sets the board_list attribute

        :param: The number of boards to generate
        :return: None
        """
        if num_of_boards == len(BOARDS):
            self.board_list = BOARDS.copy()
            return
        random_indices = random.sample(range(0, len(BOARDS)), num_of_boards)
        for index in random_indices:
            self.board_list.append(BOARDS[index])

    def _archipelagos_setup(self):
        self.archipelagos_setup = []
        total = self.number_of_players
        if self.extra_board:
            total += 1

        open_oceans = None
        while total:
            if total == 1:
                self.archipelagos_setup.append(1)
                return

            if not self.archipelagos_setup:
                island_size = random.randint(1, total - 1)
                open_oceans = island_size
            elif total == 2 and open_oceans == 1:
                island_size = 2
                open_oceans += island_size - 2
            elif open_oceans == 1:
                island_size = random.randint(2, total)
                open_oceans += island_size - 2
            else:
                island_size = random.randint(1, total)
                open_oceans += island_size - 2

            self.archipelagos_setup.append(island_size)

            total -= island_size


def construct_all_boards(num_of_players):
    """
    Constructs a list of all boards setups

    :param num_of_players: The number of Spirits playing
    :return: A list of all board setups
    """
    board_list = []
    for thematic in [True, False]:  # Thematic
        for archipelagos in [True, False]:  # Archipelagos
            for extra_board in [True, False]:  # Extra Board
                if not (num_of_players == 6 and extra_board):
                    board_list.append(Board(num_of_players, thematic, archipelagos, extra_board))

    return board_list
