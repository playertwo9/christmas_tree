height = input('height: ')
leaves_counter = 0
nothing_counter = int(height)
for i in range(int(height)):
    leaves = leaves_counter * '*'
    nothing = nothing_counter * ' ' 
    print(nothing + leaves + '*' + leaves) 
    leaves_counter += 1
    nothing_counter -= 1
    
print(int(height) * ' ' + '[]')
    