'''Description

To disarm the bomb you have to cut some wires. These wires are either white,
black, purple, red, green or orange.

The rules for disarming are simple:

If you cut a white cable you can't cut white or black cable.
If you cut a red cable you have to cut a green one
If you cut a black cable it is not allowed to cut a white, green or orange one
If you cut a orange cable you should cut a red or black one
If you cut a green one you have to cut a orange or white one
If you cut a purple cable you can't cut a purple, green, orange or white cable

If you have anything wrong in the wrong order, the bomb will explode.
There can be multiple wires with the same colour and these instructions are
for one wire at a time. Once you cut a wire you can forget about the previous
ones.

Formal Inputs & Outputs

Input description

You will receive a sequence of wires that where cut in that order and you
have to determine if the person was successful in disarming the bomb or that
it blew up.

Input 1

white
red
green
white

Input 2

white
orange
green
white

Output description

Whether or not the bomb exploded
Output 1
"Bomb defused"
Output 2
"Boom"
'''


def disarm(wires):
    valid_colors = set(['white', 'black', 'purple', 'red', 'green', 'orange'])
    for color in wires:
        if color not in valid_colors:
            return 'Boom!'
        valid_colors.clear()
        if (color == 'white'):
            valid_colors.add('purple')
            valid_colors.add('red')
            valid_colors.add('green')
            valid_colors.add('orange')
        elif (color == 'red'):
            valid_colors.add('green')
        elif (color == 'black'):
            valid_colors.add('black')
            valid_colors.add('purple')
            valid_colors.add('red')
        elif (color == 'orange'):
            valid_colors.add('black')
            valid_colors.add('red')
        elif (color == 'green'):
            valid_colors.add('orange')
            valid_colors.add('white')
        elif (color == 'purple'):
            valid_colors.add('black')
            valid_colors.add('red')

    return 'Bomb disarmed'

input1 = ['white',
          'red',
          'green',
          'white']

input2 = ['white',
          'orange',
          'green',
          'white']

print(disarm(input1))
print(disarm(input2))