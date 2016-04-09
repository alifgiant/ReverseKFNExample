class Point(object):
    def __init__(self, ord_x, ord_y):
        self.x = ord_x
        self.y = ord_y

    def __str__(self):
        return '(x,y)=> ('+str(self.x)+','+str(self.y)+')'


class Line(object):
    def __init__(self, m, c, is_horizontal):
        self.m = m
        self.c = c
        self.is_horizontal = is_horizontal

    def get_coordinate(self, x):
        y = int(self.m*x + self.c)
        return Point(x, y) if self.is_horizontal else Point(y, x)

    def __str__(self):
        if self.is_horizontal:
            return 'y = ' + str(self.m)+'x + '+str(self.c)
        else:
            return 'y\' = ' + str(self.m)+'x + '+str(self.c)


class Segment(Line):
    def __init__(self, point_a, point_b, is_horizontal=True):
        m, c = self.get_line(point_a, point_b, is_horizontal)
        super(Segment, self).__init__(m, c, is_horizontal)
        self.point_a = point_a
        self.point_b = point_b

    def get_top_point(self):
        return self.point_a if self.point_a.y < self.point_b.y else self.point_b

    def get_left_point(self):
        return self.point_a if self.point_a.x < self.point_b.x else self.point_b

    @staticmethod
    def get_line(point_a, point_b, is_horizontal=True):
        if is_horizontal:
            m = float(point_b.y - point_a.y) / (point_b.x - point_a.x)
            c = (m * (-point_a.x)) + point_a.y
        else:
            m = float(point_b.x - point_a.x) / (point_b.y - point_a.y)
            c = (m * (-point_a.y)) + point_a.x
        return m, c

    def __len__(self):
        return get_distance(self.point_a, self.point_b)


def get_distance(point_a, point_b):
        from math import sqrt
        return sqrt((point_b.x - point_a.x)**2 + (point_b.y - point_a.y)**2)


