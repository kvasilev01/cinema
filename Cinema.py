Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def order_of_seats(cinema):
	min_count = len(cinema[0]) + 1
	row = 0
	for x in range(0, len(cinema)):
		free_seats = 0
		for y in range(0, len(cinema)):
			if cinema[x][y] == 0:
				freee_seats += 1
				if free_seats < min_count and free_seats != 0:
					min_count = free_seats
					row = x + 1
		return row

	
>>> def find_col(row, cinema):
    if 0 in cinema[row]:
        return cinema[row].index(0) + 1
    else:
        return None

>>> def order_of_seats(cinema):
	result_list = []

	
>>> print(order_of_seats([[1, 1, 1], [1, 0, 0], [1, 0, 0], [1, 1, 0]]))
None
>>> 
