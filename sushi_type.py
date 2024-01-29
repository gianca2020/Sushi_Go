cards = [1] * 108

class Card(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    #the dumpling is scored based on how many dumplings are present, so one dumpling is one pont, 2=3, 3=6, 4=10, 5(and more)=15
    def dumpling(self,d):
        if d >= 5:
            return 15

        for i in range(1, d + 1):
            sum = (d + (d + 1) //2)
        return sum
    #you need to have a pair of tempura to get the neccecary amount of points
    def tempura(self, t):
        if(t !=2):
            return 0
        else:
            return 5

    def sashimi(self, s):
        if (s != 3):
            return 0
        else:
            return 10



    def nigiri(self, n):
        if self.name in ["Egg Nigiri", "Salmon Nigiri", "Squid Nigiri"]:
            base_score = {"Egg Nigiri": 1, "Salmon Nigiri": 2, "Squid Nigiri": 3}[self.name]
        if wasabi_count > 0:
            return base_score * 3  # Triple the score if Wasabi is available
        else:
            return base_score

    #def pudding(self, p):


wasabi_count = 0



