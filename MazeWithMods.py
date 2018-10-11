from Maze import*


class MazeWithMods(Maze):
    def __init__(self):
        Maze.__init__(self)
        self.mods = {}
        self.acceptable_mods = ['Water', 'Flooding', 'Waterproof', 'Trampoline', 'target', 'Growth', 'Razors']
        self.acceptable_chars_from_mods = {'Growth': 'W', 'Razors': '!',
                                           'Trampoline': 'ABCDEFGHI', 'target': '123456789'}
        # if char in acceptable_chars_from_mods['Trampoline']

    def read(self, fname):
        data, rows = Maze.read(self, fname)

        if rows < data.size:
            keys = []
            values = []
            for d in data[rows:]:
                key = d.split(' ')[0]

                if key in self.acceptable_mods:
                    keys.append(key)

                    if key == 'Trampoline':
                        pass
                        # проверяем, что 1 из списка
                        # проверяем, что след это таргет
                        # проверяем, что после таргета из списка
                    else:
                        value = d.split(' ')[1]
                        # проверяем в словаре
                else:
                    print("Unacceptable key") #todo

            self.mods = {k: v for k, v in zip(keys, values)}

