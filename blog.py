import web
class hello:
	def GET(self):
		return "hello world"

urls = ("/.*",hello)
app = web.application(urls,globals())
if __name__ == "__main__":
	app.run()
