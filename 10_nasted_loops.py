# nasted loops is a loop inside another loop. The inner loop will be executed for each iteration of the outer loop.

for i in range(1, 4):  # outer loop will run 3 times (i = 1, 2, 3)
    print(f"Outer loop iteration: {i}")
    
    for j in range(1, 4):  # inner loop will run 3 times for each iteration of the outer loop (j = 1, 2, 3)
        print(f"  Inner loop iteration: {j}")
        
        