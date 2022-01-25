colorNumPair=[]
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            colorNumPair.append(f'{i * 5 + j} | {major} | {minor}')
    return colorNumPair


result = print_color_map()
assert(result[24] == '25|Violet|Slate')
print("All is well (maybe!)\n")
