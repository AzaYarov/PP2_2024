with open('file.txt') as file:
    file_for_copy = file.read()
    
    file_to_copy = open('file1.txt', 'w')
    file_to_copy.write(file_for_copy)
    
    file_to_copy.close()