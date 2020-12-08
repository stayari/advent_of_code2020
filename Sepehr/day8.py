class Day8:
    def __init__(self):
        self.acc = 0
        self.instructions = self._format_data()
        print(self.run_instructions(self.instructions))
        for instr in self.instructions:
            print(instr)
    

    def run_instructions(self, instruction_list):
        acc = 0
        i = 0
        i_before_true = 0
        do_once_flag = True
        
        while i<len(instruction_list)-1:
            print(len(instruction_list))
            instruction = instruction_list[i]
            print(instruction, "This is the instruction")
            if instruction[3] == True:
                print("Vi får en true på: {}, med index: {}".format(instruction_list[i], i))
                print("Change on: {}, med index: {}".format(instruction_list[i_before_true], i_before_true))
                #if do_once_flag == False:
                #    return acc
                #do_once_flag = False
                # change
                #if instruction_list[i_before_true][0] == 'jmp' : instruction_list[i_before_true][0] = 'nop'
                #else: instruction_list[i_before_true][0] = 'jmp'
                #i = i_before_true
                #print("nytt värde: ", instruction_list[i])
                #do_once_flag = False
                #return

                #return acc
            instruction_list[i][3] = True
            i_before_true = i 
            if instruction[0] == 'acc':
                print("In acc")
                # operator
                if instruction[1] == '+': acc += int(instruction[2])
                else: acc -= int(instruction[2])
                i += 1
            elif instruction[0] == 'jmp':
                print("in jmp")

                if instruction_list[i][3]:
                    if instruction_list[i][0] == 'jmp' : instruction_list[i_before_true][0] = 'nop'
                    else: instruction_list[i][0] = 'jmp'
                    self._fulfix()
                if instruction[1] == '+': i += int(instruction[2])
                else: i -= int(instruction[2])
                

            elif instruction[0] == 'nop':
                print("in nop")
                i += 1
                if instruction_list[i][3]:
                    if instruction_list[i][0] == 'jmp' : instruction_list[i_before_true][0] = 'nop'
                    else: instruction_list[i][0] = 'jmp'
            print(i, "Detta är i")
        return acc
    def _fulfix(self):
        '''När vi har hittat del felaktiga instruktionen, så kör vi om allt med den nya datan. Dock måste vi göra om alla
        tags till False
        '''
        self.instructions[0][3] =20
        print(self.instructions[0][3])
        for i, _ in enumerate(self.instructions):
            #self.instructions[i][3] = False
            print(self.instructions[i][3])
        self.run_instructions(self.instructions)
    def _format_data(self):
        input = open('inputs/input_text.txt', 'r').read()
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
