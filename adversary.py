from modifier import Modifier


# A list of adversary dicts.
# level_difficulties value has the index equal to the adversary level
# Examples:
#   Brandenburg-Prussia Level 4 -> Difficulty 6
#   The Kingdom of England Level 5 -> Difficulty 9
ADVERSARIES = [
    {'name': 'Brandenburg-Prussia',
     'level_difficulties': [1, 2, 4, 6, 7, 9, 10],
     'easier_notes': ['Spirits that do not need buildup time.'],
     'harder_notes': ['Spirits that need buildup time.']},
    {'name': 'The Kingdom of England',
     'level_difficulties': [1, 3, 4, 6, 7, 9, 11],  # The community agrees that England Level 6 is Difficulty 11
     'easier_notes': ['Spirits that can destroy Towns.'],
     'harder_notes': ['Spirits that rely on killing Explorers to prevent Invader Builds.']},
    {'name': 'The Kingdom of Sweden',
     'level_difficulties': [1, 2, 3, 5, 6, 7, 8],
     'easier_notes': ['Spirits that can prevent ravages.'],
     'harder_notes': ['Spirits that have little Defence']},
    {'name': 'The Kingdom of France',
     'level_difficulties': [2, 3, 5, 7, 8, 9, 10],
     'easier_notes': ['Spirits that can destroy Towns.'],
     'harder_notes': ['Spirits that have difficulties destroying Towns.']},
    {'name': 'The Kingdom of Scotland',
     'level_difficulties': [1, 3, 4, 6, 7, 8, 10],
     'easier_notes': ['Spirits with Coastal control', 'Spirits good at destroying Buildings.'],
     'harder_notes': ['Spirits that have difficulties destroying Buildings']},
    {'name': 'The Tsardom of Russia',
     'level_difficulties': [1, 3, 4, 6, 7, 9, 11],
     'easier_notes': ['Spirits that prevent Exploring or good Explorer control.'],
     'harder_notes': ['Spirits that have a difficulties controlling Explorers.']},
    {'name': 'The Habsburg Monarchy',
     'level_difficulties': [2, 3, 5, 6, 8, 9, 10],
     'easier_notes': ['Spirits that put Blight on the island.', 'Spirits that can Isolate.'],
     'harder_notes': ['Spirits that dislike Blight', 'With Scenarios that involve keeping Invaders from reaching a '
                                                     'given place.']}
]


class Adversary(Modifier):

    def __init__(self, name, level, difficulty, easier_notes=None, harder_notes=None):
        """
        Creates an Adversary

        :param name: The name of the Adversary
        :param level: What level of the Adversary to use
        :param difficulty: The resulting difficulty number
        :param easier_notes: What makes this easier
        :param harder_notes: What makes this harder
        """
        self.name = name
        self.level = level
        self.difficulty = difficulty

        super().__init__(difficulty, easier_notes=easier_notes, harder_notes=harder_notes)

    def print(self):
        print(f'Adversary Name: {self.name}, Level: {self.level}')


def construct_all_adversaries():
    """
    Constructs a list of all adversaries with varying levels and difficulties

    :return: A list of all adversaries
    """
    adversary_list = []

    for adversary in ADVERSARIES:
        for level in range(0, 7):
            adversary_list.append(Adversary(name=adversary['name'],
                                            level=level,
                                            difficulty=adversary['level_difficulties'][level],
                                            easier_notes=adversary['easier_notes'],
                                            harder_notes=adversary['harder_notes']))

    return adversary_list
