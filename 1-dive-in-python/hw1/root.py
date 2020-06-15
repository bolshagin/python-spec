import sys

#a, b, c = 13, 236, -396
#a, b, c = 1, -3, -4
a = int(sys.argv[1]) 
b = int(sys.argv[2]) 
c = int(sys.argv[3])

x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a) 

print(int(x1), int(x2), sep='\n')
