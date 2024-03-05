class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        for i in range(0, len(nums)):
            self.result +=  (num + nums[i])
        return self
    def subtract(self, num, *nums):
        for i in range(0, len(nums)):
            self.result -= (num+nums[i])
        return self
# create an instance:
md = MathDojo()
# to test:
y= md.add(5).add(5,2).add(5,2,3,7,7).result
print(y)
z= md.subtract(5).subtract(5,2).subtract(5,2,3,7,7).result
print(z)
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5


