#!/usr/bin/env python3

from person import Person

def main():
	f = Person(10)
	print(f.getAge())
	print(f.getDecades())
	print(f.fib())
	f.setAge(51)
	print(f.getAge())
	print(f.getDecades())


if __name__ == '__main__':
	main()
