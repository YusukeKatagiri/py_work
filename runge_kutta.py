# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as plt


def runge_kutta(x0, y0, dx, endx):
	x = x0
	y = y0
	res = [[x, y]]
	while x <= endx:
		s1 = f(x, y)
		s2 = f(x + dx/2, y + dx*s1/2)
		s3 = f(x + dx/2, y + dx*s2/2)
		s4 = f(x + dx, y + dx*s3)
		x += dx
		y += (s1 + 2*s2 + 2*s3 + s4) * dx / 6
		res.append([x, y])
	return res

def f(x, y):
	return (x**2 +x + 1) - (2*x + 1)*y + y**2

def output(filename, ans):
	f = open(filename, 'w')
	for i in ans:
		f.write('%f %f\n' % (i[0], i[1]))
	f.close()

def main():
	x0 = 0.0    #初期値
	y0 = 0.5
	dx = 0.1    #刻み幅
	endx = 2.0    #終了地点
	filename = 'runge_kutta.csv'
	ans = runge_kutta(x0, y0, dx, endx)
	output(filename, ans)

if __name__ == '__main__':
	main()