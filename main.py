import math
FIGURES = [
    {'type': 'round', 'params': [3]},
    {'type': 'rectangle', 'params': [3, 4]},
    {'type': 'round', 'params': [9]},
    {'type': 'rectangle', 'params': [4, 10]},
]


def get_square(figure):
    if figure['type'] == 'round':
        return math.pi * figure['params'][0] ** 2
    elif figure['type'] == 'rectangle':
        return figure['params'][0] * figure['params'][1]


print(
    sum(
        map(
            get_square,
            FIGURES
        )
    )
)