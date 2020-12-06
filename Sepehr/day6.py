class Day6():
    """
    docstring
    """
    def __init__(self):
        self.form_answer = dict() #dictdict
        self._format_input()

    def _format_input(self):
        input = open('inputs/input6.txt', 'r')
        group_id = 0
        group_answer = dict()
        person_counter = 0 
        rows = input.readlines()
        rows.append('\n')
        for line in rows:
            if line == '\n':
                group_answer['Yes'] = len(group_answer)
                group_answer['Persons'] = person_counter
                self.form_answer[group_id] = group_answer
                group_id += 1
                group_answer = dict()
                person_counter = 0
            else:
                person_counter += 1
                for letter in line[:-1]:
                    #print(letter)
                    if letter in group_answer:
                        group_answer[letter] += 1
                    else: 
                        group_answer[letter] = 1

    def get_yes_sum(self):
        res = 0
        for key in self.form_answer:
            res += self.form_answer[key]['Yes']
        print(res)
        return res

    def get_everyone_yes(self):
        res = 0
        for key in self.form_answer:
            for letter in self.form_answer[key]:
                if letter not in ['Yes', 'Persons']:
                    if self.form_answer[key][letter] == self.form_answer[key]['Persons']:
                        res += 1 
        return res

    def print(self):
        print(self.form_answer)

if __name__ == '__main__':
    puzzle = Day6()
    puzzle.get_yes_sum()
    puzzle.print()
    print(puzzle.get_everyone_yes())
