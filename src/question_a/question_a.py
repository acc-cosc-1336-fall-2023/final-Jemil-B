#write functions here, don't add input('') statements here!
def create_multiplication_table():
    multiplication_table = []
    for i in range(1, 6):
        row = []
        for j in range(1, 11):
            row.append(i * j)
        multiplication_table.append(row)
    return multiplication_table

def display_multiplication_table(table):
    for row in table:
        print(" ".join(map(str, row)))