


def part1(data_input):
    frequency = 0
    for line in data_input:
        frequency += int(line)
    print(frequency)


def part2(data_input):
    current_frequency = 0
    frequencies = set()
    found = False
    index = 0
    while not found:
        current_frequency += data_input[index]
        if current_frequency in frequencies:
            found = True
        frequencies.add(current_frequency)
        
        index = (index+1) % len(data_input)
    print(current_frequency)


file=open("input.txt","r")
data_input = list()
for line in file:
    data_input.append(int(line))

part1(data_input)  
part2(data_input) 



