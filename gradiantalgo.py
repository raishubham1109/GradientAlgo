from numpy import *


def error(b,m,points):
	totalError = 0 	#sum of square error formula
	for i in range (0, len(points)):
		x = points[i, 0]
		y = points[i, 1]
		totalError += (y-(m*x + b)) ** 2
	return totalError/ float(len(points))


def step_gradient(b_current, m_current, points, learning_rate):
	b_gradient = 0
	m_gradient = 0
	N = float(len(points))
	for i in range(0, len(points)):
		x = points[i, 0]
		y = points[i, 1]
		b_gradient += -(2/N) * (y - (m_current * x + b_current))
		m_gradient += -(2/N) * x * (y - (m_current * x + b_current))
	new_b = b_current - (learning_rate * b_gradient)
	new_m = m_current - (learning_rate * m_gradient)
	return [new_b,new_m]

def gradient(points, starting_b, starting_m, learning_rate, iteartions):
	b = starting_b
	m = starting_m
	for i in range(iteartions):
		b,m = step_gradient(b, m, array(points), learning_rate)
	return [b,m]

def run():
	points = genfromtxt('data.csv', delimiter=',')

	learning_rate = 0.0001 #alfa
	initial_b = 0 # theat0
	initial_m = 0 # theta1
	iteartions = 1000
	print("Starting gradient descent at b = {0}, m = {1}, error = {2}".
	format(initial_b, initial_m,error(initial_b, initial_m, points)))

	print("Running...")

	[b, m] = gradient(points, initial_b, initial_m, learning_rate, iteartions)

	print("After {} iterations b = {}, m = {}, error = {}".
	format(iteartions, b, m, error(b, m, points)))


if __name__ == "__main__":
	run()
