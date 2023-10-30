""" Python interface to the C++ Person class """
import ctypes
lib = ctypes.cdll.LoadLibrary('./libperson.so')

class Person(object):
	def __init__(self, age):
		lib.Person_new.argtypes = [ctypes.c_int]
		lib.Person_new.restype = ctypes.c_void_p
		lib.Person_getAge.argtypes = [ctypes.c_void_p]
		lib.Person_getAge.restype = ctypes.c_int
		lib.Person_setAge.argtypes = [ctypes.c_void_p,ctypes.c_int]
		lib.Person_getDecades.argtypes = [ctypes.c_void_p]
		lib.Person_getDecades.restype = ctypes.c_double
		lib.Person_delete.argtypes = [ctypes.c_void_p]
		lib.Person_fib.argtypes = [ctypes.c_void_p]
		lib.Person_fib.restypes = [ctypes.c_int]
		# lib.Person_fibonacci.argtypes = [ctypes.c_int]
		# lib.Person_fibonacci.restypes = [ctypes.c_int]
		self.obj = lib.Person_new(age)

	def getAge(self):
		return lib.Person_getAge(self.obj)

	def setAge(self, age):
		lib.Person_setAge(self.obj, age)

	def getDecades(self):
		return lib.Person_getDecades(self.obj)
        
	def __del__(self):
		return lib.Person_delete(self.obj)
	
	def fib(self):
		return lib.Person_fib(self.obj)
	
	# def fibonacci(self, age):
	# 	return lib.Person_fibonacci(self.obj, age)