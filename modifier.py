class Modifier(object):

    def __init__(self, difficulty, easier_notes=None, harder_notes=None):
        """
        A base modifier object. Can optionally pass in notes

        :param difficulty: The numerical difficulty of the modifier
        :param easier_notes: A list of notes that make this modifier easier
        :param harder_notes: A list of notes that make this modifier harder
        """
        self.difficulty = difficulty
        self.easier_notes = []
        self.harder_notes = []
        if easier_notes:
            self.easier_notes = easier_notes
        if harder_notes:
            self.harder_notes = harder_notes

    def print_easier_notes(self):
        """
        Prints all of notes that make this modifier easier

        :return: None
        """
        for note in self.easier_notes:
            print(note)

    def print_harder_notes(self):
        """
        Prints all of notes that make this modifier harder

        :return: None
        """
        for note in self.harder_notes:
            print(note)

    def combination_difficulty_increase(self):
        pass

    def print(self):
        raise NotImplementedError("Modifier has not implemented print!")
