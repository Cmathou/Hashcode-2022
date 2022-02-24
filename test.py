import progressbar

# a=0

# for i in progressbar.progressbar(range(1000)):
# 	a+=1

class A:
	def __init__(self):
		self.a = 1
	def change(self):
		self.a = 2
	def geta(self):
		return self.a

b = A()

d = {"pilou":[b], "t":[b,b]}
d["pilou"][0].change()
print(b.geta())
# b.change()
print(b.geta())

print(d["pilou"][0].geta())
