def ricochet(height, width, velocity):

    def move(particle):
        particle['position'][0] += particle['direction'][0]
        particle['position'][1] += particle['direction'][1]
        particle['distance'] += 1

        if particle['position'][0] == 0:
            particle['direction'][0] = 1
            particle['bounce'] += 1
        elif particle['position'][0] == width:
            particle['direction'][0] = -1
            particle['bounce'] += 1

        if particle['position'][1] == 0:
            particle['direction'][1] = 1
            particle['bounce'] += 1
        elif particle['position'][1] == height:
            particle['direction'][1] = -1
            particle['bounce'] += 1

    def is_corner(particle):
        if particle['position'] == [0, 0]:
            particle['corner'] = 'LL'
            particle['bounce'] -= 1
        elif particle['position'] == [0, height]:
            particle['corner'] = 'UL'
            particle['bounce'] -= 1
        elif particle['position'] == [width, 0]:
            particle['corner'] = 'LR'
            particle['bounce'] -= 1
        elif particle['position'] == [width, height]:
            particle['corner'] = 'UR'
            particle['bounce'] -= 1

    particle = {
        'position': [0, height],
        'direction': [1,-1],
        'distance': 0,
        'bounce': 0,
        'corner': None,
    }

    while particle['corner'] == None:
        move(particle)
        is_corner(particle)

    particle['time'] = particle['distance'] / velocity

    return particle['corner'], particle['bounce'] - 1, particle['time']

print(ricochet(15,4,2))