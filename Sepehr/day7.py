class Day7:

    def __init__(self):
        self.bag_dict = dict()
        self.holder_bag = dict()

        self._format_data()


    def _find_gold(self, bag_color):
        depth_counter = 1
        for bag in self.bag_dict:
            self.holder_bag[bag_color] ='New color!'
            if bag_color in self.bag_dict[bag]:
                self._find_gold(bag)
                #depth_counter += self._find_gold(bag)
        return depth_counter


    def find_gold(self):
        self._find_gold('shinygoldbags')
        # Ta bort raden shinygoldbag för vi får fel med ett
        self.holder_bag.pop('shinygoldbags')
        return len(self.holder_bag)

    def find_gold_gammal(self):
        for bag in self.bag_dict:
            if 'shinygoldbags' in self.bag_dict[bag]:
                self._find_gold(bag)
                #gold_counter += self._find_gold(bag)
        return len(self.holder_bag)
        #print(gold_counter)


    def _format_data(self):
        input = open('inputs/input7.txt', 'r')
        for line in input.readlines():
            # Shitty code w/e
            line = line.replace(' ', '').replace('.', '').strip()
            bag_info = line.split('contain')
            if bag_info[1] == 'nootherbags':
                print('tom väska')
            else: 
                bag_info[1:] = bag_info[1].split(',')
            self._add_bag_info(bag_info)
        self.find_gold()

    def _add_bag_info(self, bags):
        inner_bag = dict()
        if bags[1] == 'nootherbags':
            self.bag_dict[bags[0]] = {bags[1]: 0}
            return
        for bag in bags[1:]:
            bag_color = bag[1:]
            if bag[0] == '1': bag_color = bag_color + 's' #concatinate 's' for plural cornercase
            inner_bag[bag_color] = bag[0]
        self.bag_dict[bags[0]] = inner_bag

    def print(self):
        for k in self.bag_dict:
            print(k, ':', self.bag_dict[k])

if __name__ == '__main__':
    puzzle = Day7()
    #puzzle.print()
    print(len(puzzle.holder_bag))
