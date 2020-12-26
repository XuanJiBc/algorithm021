class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        obs = set(map(tuple, obstacles))
        x = y = dr = res = 0
        for cmd in commands:
            if cmd == -2:
                dr = (dr - 1) % 4
            elif cmd == -1:
                dr = (dr + 1) % 4
            else:
                for i in range(cmd):
                    if (x + dx[dr], y + dx[dr]) not in obs:
                        x += dx[dr]
                        y += dy[dr]
                        print(x, y)
                        res = max(res, x*x + y*y)
        return res