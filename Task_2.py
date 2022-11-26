class Table():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.a = [[0] * y for i in range(x)]
 
    def get_value(self, x, y):
        if 0 <= x < self.x and 0 <= y < self.y:
            return self.a[x][y]
        else:
            return None
 
    def delete_row(self, row):
        self.a.pop(row)
        self.x -= 1
 
    def n_cols(self):
        return self.y 
 
    def set_value(self, x, y, a):
        self.a[x][y] = a
 
    def n_rows(self):
        return self.x
 
    def add_row(self, row):
        self.a.insert(row, [0] * self.y)
        self.x += 1
 
    def add_col(self, col):
        for row in range(self.x):
            self.a[row].insert(col, 0) 
        self.y += 1
 
    def delete_col(self, y):
        for i in range(self.x):
            self.a[i].pop(y) 
        self.y -= 1
