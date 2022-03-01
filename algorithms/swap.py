class swap:
    def yah(self, ah):
        print(self, ah)
        if self < ah:
            return self, ah
        else:
            x = self
            self = ah
            ah = x
            return self, ah

    a, b = yah(21, 16)
    print(a, b)
