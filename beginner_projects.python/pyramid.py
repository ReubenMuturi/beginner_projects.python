x = "#"
row = 0
counter = 8
rows = []
i = 8
y = 0


def arrange(r, column):
    return " " * (column - r + 8) + x * (2 * r - 1)


while i > row:
    i -= 1
    rows.append((arrange(i, row)))


def arrange1(r1, column1):
    return " " * (column1 - r1) + x * (2 * r1 - 1)


while y < counter:
    y += 1
    rows.append((arrange1(y, counter)))

display = ""

for row in rows:
    display += "\n" + row

print(display)


