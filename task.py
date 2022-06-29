class piecewise_func:

    def __init__(self, x=None, y=None):

        self._points = dict()
        if None not in (x, y):
            self._points[x] = y

    def __call__(self, x, y):
        self._points[x] = y
        return self

    def y(self, x):
        x1, x2 = self._find_interval(x)
        y1, y2 = self._points[x1], self._points[x2]
        if x1 == x2:
            return self._points[x1]
        return (x-x1)*(y2-y1)/(x2-x1) + y1

    def table(self):
        x_sorted = sorted([xp for xp in self._points])
        print('--------------------------')
        print('|  x1  |  x2  |  a  |  b  |')
        for i in range(len(x_sorted)-1):
            x1, x2 = x_sorted[i], x_sorted[i+1]
            y1, y2 = self._points[x1], self._points[x2]
            a = -(y2-y1)/(x1-x2)
            b = -(x2*y1 - x1*y2)/(x1-x2)
            print('--------------------------')
            print(f'|  {x1}  |  {x2}  |  {a}  |  {b}  |')

    def _find_interval(self, x):
        x_points = [xp for xp in self._points]
        left, right = min(x_points), max(x_points)
        for seek_x in x_points:
            if seek_x <= x:
                left = max(left, seek_x)
            elif seek_x > x:
                right = min(right, seek_x)
        return left, right


F = piecewise_func(0, 100)(10, 122)
F = F(30, 0)
print(F.y(5))
F.table()
