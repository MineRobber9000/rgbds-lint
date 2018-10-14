import util,re

class Keys:
	FUNCTION_DECLARATION = "[^;]+(:{1,2})"
	IGNORE_LINE = "; ignore: (.*)$"
	@classmethod
	def combine(cls,*args):
		regexen = [getattr(cls,a) if hasattr(cls,a) else util.raiseerror(Exception,"Unknown key {}".format(a)) for a in args]
		return "("+"|".join(regexen)+")"

class ParsedFunc:
	def __init__(self,code,ignores=[]):
		self.code = code
		self.ignores = ignores

	def lint(self):
		pass

if __name__=="__main__":
	with open("test.asm") as f:
		lines = [l.rstrip() for l in f]
	func_dec = util.matchinglines(lines,Keys.FUNCTION_DECLARATION)
	assert len(func_dec)==1,"Too many lines matched function declaration regex"
	print("Function declaration:",func_dec)
	func_dec = func_dec[0]
	ignore_line = util.walkback(lines,func_dec,Keys.IGNORE_LINE)
	print("ignore directive:",ignore_line)
	end = util.walkup(lines,func_dec+1,Keys.combine("FUNCTION_DECLARATION","IGNORE_LINE"))
	if end is None:
		end = -1
	print("Code:",lines[func_dec:end])
	print("Ignores:",re.match(Keys.IGNORE_LINE,lines[ignore_line]).group(1).split(", "))
