class Day8:
    def __init__(self):
        self.acc = 0
        self.instructions = self._format_data()
        self.run_instructions(self.instructions)

    def run_instructions(self, instruction_list):
        acc = 0
        i = 0 
        while i<len(instruction_list):
            instruction = instruction_list[i]
            print(instruction, "This is the instruction")
            if instruction[3] == True:
                print("Får vi en true??", instruction_list[i])
                print("Returning acc+1", acc)
                return acc
            instruction_list[i][3] = True

            if instruction[0] == 'acc':
                print("In acc")
                # operator
                if instruction[1] == '+': acc += int(instruction[2])
                else: acc -= int(instruction[2])
                i += 1
            elif instruction[0] == 'jmp':
                print("in jmp")
                if instruction[1] == '+': i += int(instruction[2])
                else: i -= int(instruction[2])
                
            elif instruction[0] == 'nop':
                print("in nop")
                i += 1
            print(i, "Detta är i")
        return
    def _format_data(self):
        input = open('inputs/input8.txt', 'r').read()
        instruction_lines = input.split('\n')
        print(instruction_lines)
        for i, instruction in enumerate(instruction_lines):
            operator = self._get_operator(instruction)
            sign = self._get_sign(instruction)
            nbr = self._get_nbr(instruction)
            executed = False
            instruction_lines[i] = [operator, sign, nbr, executed]
        return instruction_lines
    def _get_nbr(self, instruction):
        return instruction[5:]
    def _get_sign(self, instruction):
        return instruction[4]
    def _get_operator(self, instruction):
        return instruction[:3]

        

if __name__ == '__main__':
    puzzle = Day8()
    tal = '123456789'
    print(tal[:3])
