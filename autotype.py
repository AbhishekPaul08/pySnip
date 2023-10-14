from pynput.keyboard import Key, Controller
import time

keyboard= Controller()

def auto(n):
    time.sleep(5)
    for i in n.split("\n"):
        keyboard.type(i)
        keyboard.press(Key.enter)
        time.sleep(0.01)

# code to auto type in your editor
n='''
# # Python3 program for the above approachcodeiscontributedbym
# from math import sqrt, floor, ceil

# # Function that returns True if N
# # is a perfect square
# def isPerfectSquare(N):

# 	floorSqrt = floor(sqrt(N))
# 	return (N == floorSqrt * floorSqrt)

# # Function that returns True check if
# # N is sum of three squares
# def legendreFunction(N):

# 	# Factor out the powers of 4
# 	while (N % 4 == 0):
# 		N //= 4

# 	# N is NOT of the
# 	# form 4^a * (8b + 7)
# 	if (N % 8 != 7):
# 		return True
# 	else:
# 		return False

# # Function that finds the minimum
# # number of square whose sum is N
# def minSquares(N):

# 	# If N is perfect square
# 	if (isPerfectSquare(N)):
# 		return 1

# 	# If N is sum of 2 perfect squares
# 	for i in range(N):
# 		if i * i < N:
# 			break
# 		if (isPerfectSquare(N - i * i)):
# 			return 2

# 	# If N is sum of 3 perfect squares
# 	if (legendreFunction(N)):
# 		return 3
	
# 	# Otherwise, N is the
# 	# sum of 4 perfect squares
# 	return 4

# # Driver code
# if __name__ == '__main__':

# 	# Given number
# 	N = 123

# 	# Function call
# 	print(minSquares(N))
'''
auto(n) #this function is to call


