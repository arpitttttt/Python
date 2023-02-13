
i = 100
while (i <= 400) :
    y = i
    count = 0
    while (y != 0) :
     if ((y % 10) % 2 == 0) :
        count += 1
        y /= 10
        if (count == 3) :
                print(str(i) + ",", end ="")
        i += 1