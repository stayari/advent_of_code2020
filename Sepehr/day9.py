class Day9:

    def __init__(self):
        self.preambl_len = 26
        self.data = self.read_data()
        error = self.find_first_wrong(self.data)
        print(error)
        result = self._find_set_equals(error)
        print('Result for part 1: {} \nResult för part 2: {}'.format(error, result))
        #print('Start index: {} Stop index: {}'.format(self.data[start], self.data[stop]))
        #print("adding: ",int(self.data[start])+int(self.data[stop] ))

    def _find_set_equals(self, error):
        ''' finds a contingious set in data that adds up to the error. Returns the sum of the minimum and max value in the set'''
        for i in range(len(self.data)):
            sum_set = int(self.data[i])
            j = i+1
            while sum_set < error:
                sum_set += int(self.data[j])
                if sum_set == error:
                    return_set = list(map(int,self.data[i:j]))
                    return min(return_set)+max(return_set)
                j += 1

    def read_data(self):
        input = open('inputs/input9.txt', 'r').read()
        instruction_lines = input.split('\n')
        return instruction_lines

    def find_first_wrong(self, data_list):
        preamble = self.data[:self.preambl_len]
        i = 0
        while i< len(self.data):
            i += 1
            if self._check_if_valid(preamble):
                print("in baby")
                preamble = self.data[i:i+self.preambl_len]
                print(preamble)
            else:
                return int(preamble[-1])

    def _check_if_valid(self, preamble):
        for i in range(len(preamble)-1):
            for j in range(1,len(preamble)-1):
                if i != j: 
                    if int(preamble[i]) + int(preamble[j]) == int(preamble[-1]):
                        print("print preambl",preamble[-1])
                        return True
        return False


if __name__ == '__main__':
    puz = Day9()
    l = puz.data
    #ll = []
    #print("hej",ll[-1])
    
