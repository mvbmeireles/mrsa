class roboMRSA():
    def mrsa(self, command):
        position = [0, 0, 'N']
        strCommand = str(command)
        for i in strCommand:
            if i == 'L':
                if position[2] == 'N':
                    position[2] = 'W'
                elif position[2] == 'W':
                    position[2] = 'S'
                elif position[2] == 'S':
                    position[2] = 'E'
                elif position[2] == 'E':
                    position[2] = 'N'
            elif i == 'R':
                if position[2] == 'N':
                    position[2] = 'E'
                elif position[2] == 'E':
                    position[2] = 'S'
                elif position[2] == 'S':
                    position[2] = 'W'
                elif position[2] == 'W':
                    position[2] = 'N'
            elif i == 'M':
                if position[2] == 'N' and position[1] != 4:
                    position[1] += 1
                elif position[2] == 'N' and position[1] == 4:
                    return ("400 Bad Request", 400)
                if position[2] == 'S' and position[1] != 0:
                    position[1] -= 1
                elif position[2] == 'S' and position[1] == 0:
                    return ("400 Bad Request", 400)
                if position[2] == 'E' and position[0] != 4:
                    position[0] += 1
                elif position[2] == 'E' and position[0] == 4:
                    return ("400 Bad Request", 400)
                if position[2] == 'W' and position[1] != 0:
                    position[0] -= 1
                elif position[2] == 'W' and position[1] == 0:
                    return ("400 Bad Request", 400)
        return f'({position[0]}, {position[1]}, {position[2]})'