import web
from calculate import fibonacci, rearrange


urls = (
    "/", "index",
    "/fibonacci/(.*)", "fibonacc"
)

class index:
	def GET(self):
		return 'Fibonacci web service. Append the url with /fibonacci/<number> to generate the series.'

# Input a number (num)
# Verify (num) is an integer greater than 0 
# 	If error, return exception message
# 	If valid entry, call fibonacci(num)
class fibonacc:
    def GET(self, num):
        try:
            num = int(num)
            series = fibonacci(num)
            sortedArr = rearrange(series)
        except ValueError as e:
            return """{\n"Exception":"%s"\n}""" % (e)
        return "fibonacci:" "%s" % (series) + "\n" + "sorted:" "%s" % (sortedArr) 
def main():
	serv = web.application(urls, globals())
	serv.run()

if __name__ == '__main__':
    main()