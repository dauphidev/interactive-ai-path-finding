import random

class PQmin (object):

    def __init__ (self):

        self.elements = []

    def add (self, ele):
        self.elements.append(ele)

    def pop_smallest (self):
        smallest_point = self.elements[0]
        for ele in self.elements:
            cost = ele.acc_cost
            if cost < smallest_point.acc_cost:
                smallest_point = ele
        self.elements.remove(smallest_point)
        return smallest_point
                
        
    def __str__ (self):
        acc_string = ["UNORDERED: "]
        for point in self.elements:
            acc_string.append("<" + str(point.pos) +"," + str(point.acc_cost) + ">" + " ")

        return "".join(acc_string)

    def extend (self, elements):
        for ele in elements:
            self.add(ele)

    def shuffle (self):
        #Method for debugging
        random.shuffle(self.elements)

    def remove (self, ele):
        self.elements.remove(ele)












        
            
            
