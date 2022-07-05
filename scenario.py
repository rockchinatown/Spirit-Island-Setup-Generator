from modifier import Modifier


SCENARIOS = [
    {'name': 'Blitz',
     'difficulty': 0,
     'easier_notes': None,
     'harder_notes': ['Spirits that need buildup time.', 'If paired with Brandenburg-Prussia Adversary.']},
    {'name': 'Dahan Insurrection',
     'difficulty': 4,
     'easier_notes': ['Spirits with versatile Dahan movement.', 'Spirits good at moving/destroying Buildings.'],
     'harder_notes': ['When paired with Adversaries that Build a lot of buildings.']},
    {'name': "Guard the Isle's Heart",
     'difficulty': 0,
     'easier_notes': ['Spirits with Build prevention.'],
     'harder_notes': ['Spirits with no Build prevention or no Fast way to deal with Explorers.',
                      'When paired with Adversaries who act quickly.',
                      'When paired with The Habsburg Monarchy Adversary.']},
    {'name': 'Rituals of Terror',
     'difficulty': 3,
     'easier_notes': ['Spirits with strong Dahan movement.', "When playing with Stone's Unyielding Defiance Spirit."],
     'harder_notes': ['In a solo game with a Spirit with poor Energy or poor Presence movement.']},
    {'name': 'Despicable Theft',
     'difficulty': 2,
     'easier_notes': ['Spirits with strong movement and Isolate abilities.'],
     'harder_notes': ['Spirits with poor Dahan movement.', 'Spirits with poor ability to Damage or move Invaders.',
                      'Paired with Thematic Board (spawns more Thieves).']},
    {'name': 'The Great River',
     'difficulty': 3,
     'easier_notes': ['When playing on Boards A and E.', 'Spirits that can destroy Inland Towns.'],
     'harder_notes': ['Boards B, C, and F, then D are most balanced.',
                      'Teams with little early control of Inland Towns.',
                      'Spirits that focus on defense/counterattacking.',
                      'When paired with Adversaries that create extra Towns.']},
    {'name': 'Ward the Shores',
     'difficulty': 2,
     'easier_notes': ['Spirits strong along the coastline.'],
     'harder_notes': ['When paired with Adversaries that bring Invader Stage III faster.']},
    {'name': 'Elemental Invocation',
     'difficulty': 0,
     'easier_notes': ['Spirits with Innate Powers that benefit from a 1 Element boost.',
                      'Spirits with efficient high level Innate Powers.',
                      'Veteran players'],
     'harder_notes': ['New players', 'Spirits which use few or no Elements for land-targeting Powers.',
                      'Spirits with tight Energy income.']},
    {'name': 'A Diversity of Spirits',
     'difficulty': 0,
     'easier_notes': ['When playing with familiar players and all Spirits in play.'],
     'harder_notes': ['Playing with unfamiliar Spirits.', 'Spirits with restrictive Presence placement.']},
    {'name': 'Varied Terrains',
     'difficulty': 2,
     'easier_notes': ['Spirits with good Build prevention in Jungles and Wetlands.'],
     'harder_notes': ['When paired with Adversaries that cause many Builds.']},
    {'name': 'Rituals of the Destroying Flame',
     'difficulty': 3,
     'easier_notes': ['Spirits that generate Energy well.'],
     'harder_notes': ['Spirits that rely heavily on Damage/Destruction.']},
    {'name': 'Powers Long Forgotten',
     'difficulty': 1,
     'easier_notes': ['Spirits with good Dahan movement.'],
     'harder_notes': ['Swingier than normal Scenario.']},
]


class Scenario(Modifier):

    def __init__(self, name, difficulty, easier_notes=None, harder_notes=None):
        """
        Creates a Scenario

        :param name: The name of the Scenario
        :param difficulty: The difficulty number
        :param easier_notes: What makes this easier
        :param harder_notes: What makes this harder
        """
        self.name = name
        self.difficulty = difficulty

        super().__init__(difficulty, easier_notes=easier_notes, harder_notes=harder_notes)

    def print(self):
        print(f'Scenario Name: {self.name}')


def construct_all_scenarios():
    """
    Constructs a list of all scenarios

    :return: A list of all scenarios
    """
    scenario_list = []

    for scenario in SCENARIOS:
        scenario_list.append(Scenario(name=scenario['name'],
                                      difficulty=scenario['difficulty'],
                                      easier_notes=scenario['easier_notes'],
                                      harder_notes=scenario['harder_notes']))
    return scenario_list