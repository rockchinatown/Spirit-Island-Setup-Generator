import board
import adversary
import scenario


class GameSetup(object):

    def __init__(self, setup_board, setup_adversary=None, setup_scenario=None, setup_second_adversary=None):
        """
        A game setup that contains which board pieces to use plus optional adversaries and scenarios

        :param setup_board: The Board object for the game
        :param setup_adversary: The Adversary object for the game
        :param setup_scenario: The Scenario object for the game
        :param setup_second_adversary: The Second Adversary for the game
        """
        self.board = setup_board
        self.adversary = setup_adversary
        self.scenario = setup_scenario
        self.second_adversary = setup_second_adversary
        self.notes = []

        self.difficulty = self.board.difficulty
        if self.scenario:
            self.difficulty += self.scenario.difficulty
        if self.second_adversary:
            self._double_adversary_setup()
        elif self.adversary:
            self.difficulty += self.adversary.difficulty

        self._extra_board_setup()

    def _extra_board_setup(self):
        """
        Calculates the difficulty for the extra board if there is one and sets the difficulty attribute

        :return: None
        """
        # Lastly, check the extra board modifier
        if self.board.extra_board:
            if self.difficulty <= 2:
                self.difficulty += 2
            elif self.difficulty <= 5:
                self.difficulty += 3
            else:
                self.difficulty += 4
            if self.second_adversary:
                if 'The Kingdom of France' in self.adversary.name:
                    self.notes.append('Base the size of the Towns pool off of the number of boards, not players.')
            elif self.adversary:
                if 'The Kingdom of France' in self.adversary.name:
                    self.notes.append('Base the size of the Towns pool off of the number of boards, not players.')

    def _double_adversary_setup(self):
        """
        Calculates the difficulty for a second Adversary by taking 50-75% of the following Adversary. Takes a higher
        percent as the following Adversary difficulty rises. Sets the difficulty attribute itself. Also adds any
        complicated setup notes to the easier notes.

        :return: None
        """
        leading_difficulty = max(self.adversary.difficulty, self.second_adversary.difficulty)
        following_difficulty = min(self.adversary.difficulty, self.second_adversary.difficulty)
        self.difficulty += leading_difficulty

        if following_difficulty < 3:
            self.difficulty += round(.5 * following_difficulty)
        elif following_difficulty < 7:
            self.difficulty += round(.625 * following_difficulty)
        else:
            self.difficulty += round(.75 * following_difficulty)

        if "The Kingdom of Scotland" in [self.adversary.name, self.second_adversary]:
            self.notes.append("When playing with The Kingdom of Scotland, if the other Adversary setup would add a city"
                              " to a Coastal land other than land #2, instead add the city to an adjacent Inland land.")
        if "The Kingdom of France" in [self.adversary.name, self.second_adversary]:
            self.notes.append("When playing against France Level 2 or higher, increase the pool of available Towns by 1"
                              " per player for each level of the other Adversary being played.")

    def print(self):
        print('\n\n\n================ Setup ==================')
        print(f'Difficulty: {self.difficulty}')
        self.board.print()
        if self.adversary:
            self.adversary.print()
        if self.second_adversary:
            self.second_adversary.print()
        if self.scenario:
            self.scenario.print()
        self._print_notes()

    def _print_notes(self):
        print('\n================ Notes ==================')
        for note in self.notes:
            print(note)
        print("Easier Notes: ")
        if self.board:
            self.board.print_easier_notes()
        if self.adversary:
            self.adversary.print_easier_notes()
        if self.scenario:
            self.scenario.print_easier_notes()
        print("\nHarder Notes: ")
        if self.board:
            self.board.print_harder_notes()
        if self.adversary:
            self.adversary.print_harder_notes()
        if self.scenario:
            self.scenario.print_harder_notes()


def construct_all_board_setups(num_of_players, single_adversary_only=False, no_scenario=False):
    """
    Constructs all possible board setups given the number of players. A dict is returned with the difficulty as
    the key and the value is a list of setups that match the given difficulty

    :param num_of_players: Number of Spirits playing
    :param single_adversary_only: If True, only add single adversary setups
    :param no_scenario: If True, does not include scenarios in setups
    :return: A dict of all possible board setups
    """
    board_setup_dict = {}
    for x in range(0, 30):  # 29 is the highest difficulty possible
        board_setup_dict[x] = []
    all_boards_list = board.construct_all_boards(num_of_players)
    all_adversaries_list = adversary.construct_all_adversaries()
    all_scenarios_list = scenario.construct_all_scenarios()

    # All setups must contain a board setup because it contains which board letters to use
    for unique_board in all_boards_list:
        # Only board modifiers
        setup = GameSetup(unique_board)
        board_setup_dict[setup.difficulty].append(setup)

        # Board and Adversary
        for unique_adversary in all_adversaries_list:
            setup = GameSetup(unique_board, setup_adversary=unique_adversary)
            board_setup_dict[setup.difficulty].append(setup)

        if not no_scenario:
            # Board and Scenario
            for unique_scenario in all_scenarios_list:
                setup = GameSetup(unique_board, setup_scenario=unique_scenario)
                board_setup_dict[setup.difficulty].append(setup)

        if not no_scenario:
            # Board, Adversary, and Scenario
            for unique_adversary in all_adversaries_list:
                for unique_scenario in all_scenarios_list:
                    setup = GameSetup(unique_board, setup_adversary=unique_adversary, setup_scenario=unique_scenario)
                    board_setup_dict[setup.difficulty].append(setup)

        if not single_adversary_only:
            # Board and double Adversary
            for unique_adversary in all_adversaries_list:
                for second_adversary in all_adversaries_list:
                    if unique_adversary.name != second_adversary.name:
                        setup = GameSetup(unique_board, setup_adversary=unique_adversary,
                                          setup_second_adversary=second_adversary)
                        board_setup_dict[setup.difficulty].append(setup)

            if not no_scenario:
                # Board, Scenario, and double Adversary
                for unique_adversary in all_adversaries_list:
                    for unique_scenario in all_scenarios_list:
                        for second_adversary in all_adversaries_list:
                            if unique_adversary.name != second_adversary.name:
                                setup = GameSetup(unique_board, setup_adversary=unique_adversary,
                                                  setup_scenario=unique_scenario,
                                                  setup_second_adversary=second_adversary)
                                board_setup_dict[setup.difficulty].append(setup)

    return board_setup_dict
