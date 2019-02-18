man = []
other = []
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role,line_spoken) = each_line.split(':',1)
            line_spoken = line_spoken.strip() #strip removes unwanted white spaces
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other man':
                other.append(line_spoken)
        except ValueError:
            pass
            
       
    data.close()
except IOError:
    pass
print(man)
print(other)
    
                         
            
        
