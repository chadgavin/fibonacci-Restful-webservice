def valid_input(i):
    #checks proper formating of value
	try:
		float(i) # for int, long and float
	except ValueError:
		try:
			complex(i) # for complex
		except ValueError:
			return False
	if i == int(i):
		return True
	return False


def fib():
	x, y = 0, 1
	while 1:
		yield x
		x, y = y, x + y


def fibonacci(fib_length):
    if fib_length > 100:
        raise ValueError("INVALID Input - Enter a value < 100 ")
    if not valid_input(fib_length):
        raise ValueError("INVALID Entry:  not an integer")
    if fib_length < 1:
        raise ValueError("INVALID Input - Enter a value > 0 ")
    series = []
    x = fib()
    for i in range(fib_length):
        series.append(next(x))
    return series

def rearrange(series):
    # create evenArr[] and oddArr[] 
    evenArr = [] 
    oddArr = [] 
    # Put elements in oddArr[] and evenArr[] as per their position as there are already arranged in accending order
    for i in range(len(series)): 
        if ((series[i] % 2) == 0): 
            evenArr.append(series[i]) 
        else: 
            oddArr.append(series[i])
    # Reverse order of arrays in desending order

    evenArr = evenArr[::-1] 
    oddArr = oddArr[::-1]
    arr = evenArr + oddArr
    return arr