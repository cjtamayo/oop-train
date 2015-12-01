#assignments file with class solutions

class MaxSizeList(object):
    def __init__(self, limit):
        self.limit = limit
        self.msl = []
        
    def push(self, add):
        if len(self.msl) <self.limit:
            self.msl.append(add)
        else:
            self.msl.pop(0)
            self.msl.append(add)
            
    def get_list(self):
        return self.msl
        
        
    def prinlim(self):
        print self.limit
