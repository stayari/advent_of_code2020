class Day10:

    def __init__(self):
        self.tree_stuff = []
        self.jolt_adapters = self.read_data()
        self.diff_1 = 0
        self.diff_2 = 0
        self.diff_3 = 0
        self.total_combinations = 1
        self.calc_all_combinations()
        print(self.jolt_adapters)
        self.calculate_diffs()

    def read_data(self):
        input = open('inputs/input_text.txt', 'r').read()
        instruction_lines = input.split('\n')
        # Add 0 in front for the "wall adapter"

        instruction_lines = list(map(int, instruction_lines))
        instruction_lines.sort()
        instruction_lines.insert(0,0)

        
        return instruction_lines
    
    def calculate_diffs(self):
        for i in range(len(self.jolt_adapters)-1):
            diff = self.jolt_adapters[i+1] - self.jolt_adapters[i]
            if diff == 1:
                #print('diff_1 index: {}'.format(i))
                self.diff_1 += 1
            elif diff == 2:
                print('diff_2 index: {}'.format(i))
                #self.diff_2 += 1
            elif diff ==3:
                #print('diff_3 index: {}'.format(i))
                self.diff_3 += 1
            else:
                print("Else, något är nog fel")
        # Since we have +3 in the end cuz of built in adapter. I dont get it really
        self.diff_3 += 1
    def calc_all_combinations(self):
        print("inne")
        for i in range(len(self.jolt_adapters)-3):
            comb = 1
            diff_1 = self.jolt_adapters[i+1] - self.jolt_adapters[i]
            diff_2 = self.jolt_adapters[i+2] - self.jolt_adapters[i]
            diff_3 = self.jolt_adapters[i+3] - self.jolt_adapters[i]
            if diff_1 == 2 or diff_1 == 3:
                comb += 0
            if diff_2 == 2 or diff_2 == 3: 
                comb += 1
            if diff_3 == 2 or diff_3 == 3: 
                comb += 1
            print ("From: {}, {} combinations".format(self.jolt_adapters[i], comb))
            if comb != 1:
                self.total_combinations = self.total_combinations  + comb
            self.tree_stuff.append(comb)



    def get_all_comb(self):
        comb = 1
        while i < len(self.tree_stuff)-2: 
        
        #for i in range(len(self.tree_stuff)-2):
            num_i0 = self.tree_stuff[i]
            num_i1 = self.tree_stuff[i+1]
            num_i2 = self.tree_stuff[i+2]
            num_i3 = self.tree_stuff[i+3]
            if num == 3:
                comb *= num_i0*((num_i1/num_i0)+(num_i2/num_i0)+(num_i3/num_i0))
                print("Case 3. 0: {} 1: {} 2: {} 3: {}".format(num_i0,num_i1,num_i2,num_i3))
            elif num == 2:
                stop = 0 
            
    def print(self):
        print('diff_1: {} \ndiff_2: {} \ndiff_3: {}'.format(self.diff_1, self.diff_2, self.diff_3))
        print('diff_1 * diff_3 = {}'.format(self.diff_1*self.diff_3))
        print("total combinations is: {}".format(self.total_combinations))
        print(self.tree_stuff)


if __name__ == '__main__':
    puzzle = Day10()
    puzzle.print()
    