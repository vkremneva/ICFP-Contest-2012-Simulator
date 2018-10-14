from Maze import*


class MazeWithMods(Maze):
    def __init__(self):
        Maze.__init__(self)
        self.mods = {}
        self.acceptable_mods = ['Water', 'Flooding', 'Waterproof', 'Trampoline', 'targets', 'Growth', 'Razors']
        self.acceptable_chars_from_mods = ['W', '!', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', '1', '2', '3',
                                           '4', '5', '6', '7', '8', '9']
        self.acceptable_mods_values = {'Trampoline': 'ABCDEFGHI', 'targets': '123456789'}

    def read(self, fname):
        # read maze
        data = np.loadtxt(fname, dtype=str, delimiter='\n', comments=None, usecols=0)
        print(data)
        rows = 0
        for d in data:
            if (d[0] == '#') | (d[0] == 'L') | (d[0] == ' '):
                rows += 1

        max_len = len(max(*data, key=len))

        self.maze = np.empty(shape=(rows, max_len), dtype=str)
        for i in range(rows):
            for j, ch in enumerate(data[i]):
                if (ch in self.acceptable_chars) | (ch in self.acceptable_chars_from_mods):
                    self.maze[i][j] = ch
                else:
                    print("Unacceptable char ", ch)  # todo

        print(self.maze)

        # read mods
        if rows < data.size:
            keys = []
            values = []
            ind = 1
            for d in data[rows:]:
                splits = d.split(' ')

                key = splits[0]
                if key in self.acceptable_mods:
                    if key == 'Trampoline':
                        keys.append(key + str(ind))

                        value = splits[1]
                        if value in self.acceptable_mods_values['Trampoline']:
                            values.append(value)
                        else:
                            print('Unacceptable value in Trampoline mod')  # todo

                        key = splits[2]
                        if key == 'targets':
                            keys.append(key + str(ind))
                            value = splits[3]
                            if value in self.acceptable_mods_values['targets']:
                                values.append(value)
                            else:
                                print('Unacceptable value in trampoline mod')  # todo
                        else:
                            print('Mod targets after mod trampoline not found')  # todo

                        ind += 1
                    else:
                        keys.append(key)
                        values.append(splits[1])
                else:
                    print("Unacceptable key")  # todo

            self.mods = {k: v for k, v in zip(keys, values)}

            print(self.mods)


maze = MazeWithMods()
maze.read('maps\\beard5.map')
