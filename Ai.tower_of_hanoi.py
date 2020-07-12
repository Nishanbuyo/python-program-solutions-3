def tower_of_hanoi(n, source, destination, auxilliary):
    if n == 1:
        print ("Move disk 1 from source", source, "to destination", destination)
        return
    tower_of_hanoi(n-1, source, auxilliary, destination)
    print ("Move disk", n, "from source", source, "to destination", destination)
    tower_of_hanoi(n-1, auxilliary, destination, source)


n=4
tower_of_hanoi(n,'A','B','C')  
