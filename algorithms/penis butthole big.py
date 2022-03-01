class swap:
    def poop(brown, green):
        if brown < green:
            return brown,green
        else:
            x = brown
            brown = green
            green = x
            return brown, green
        a, b = poop(1234, 1234)
        print(a, b)