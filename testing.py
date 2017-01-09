__author__ = 'fissalalsharef'

"""def set(self, col, row, v, lock=False):
    if v == self.grid[row][col] or (col, row) in self.locked:
        return
    for v2 in self.get_row(row):
        if v == v2:
            raise ValueError()
    for v2 in self.get_cols(col):
        if v == v2:
            raise ValueError()
    for y in self.get_nearest_region(col, row):
        for x in y:
            if v == x:
                raise ValueError()
    self.grid[row][col] = v
    if lock:
        self.locked.append((col, row))

"""



