class Day7:

    def __init__(self):
        self.bag_dict = dict()
        self.bag_containing_spec_color = dict()
        self._format_data()
        self.color_to_find = 'shinygoldbags'
        self.total_bags_in_gold()


    def total_bags_in_gold(self):
        res = self._total_bags_in_gold('shinygoldbags')
        print(res)
        return res

    def _total_bags_in_gold(self, bag_color):
        total_bags = 0
        for bag in self.bag_dict[bag_color]:
            if bag == 'nootherbags':
                print ("returning from rec on color.{}".format(bag_color)) 
                return 0
            total_bags = total_bags + int(self.bag_dict[bag_color][bag]) * (self._total_bags_in_gold(bag) +1)
        return total_bags

    def _find_gold(self, bag_color):
        depth_counter = 1
        for bag in self.bag_dict:
            self.bag_containing_spec_color[bag_color] ='New color!'
            if bag_color in self.bag_dict[bag]:
                self._find_gold(bag)
                #depth_counter += self._find_gold(bag)
        return depth_counter

    def find_gold(self):
        self._find_gold('shinygoldbags')
        # Ta bort raden shinygoldbag för vi får fel med ett
        self.bag_containing_spec_color.pop('shinygoldbags')
        print(self.bag_containing_spec_color)
        return len(self.bag_containing_spec_color)

    def _format_data(self):
        input = open('inputs/input7.txt', 'r')
        for line in input.readlines():
            # Shitty code w/e
            line = line.replace(' ', '').replace('.', '').strip()
            bag_info = line.split('contain')
            # If line contains 'nootherbags' there will be no ','
            if bag_info[1] != 'nootherbags':
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
    print(len(puzzle.bag_containing_spec_color))
