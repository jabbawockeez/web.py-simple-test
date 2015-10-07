import web, settings

render = settings.render
session = web.ctx.session

class login(object):
	"""docstring for login"""
	def GET(self):
		if session.username != "guest":
			raise web.seeother('/success')
		else:
			return render.login()
			
	def POST(self):
		i = web.input()

		username = i.username
		password = i.password

		# check if the username and password is correct

		session.username = username

		return render.success(username)

class logout(object):
	def GET(self):
		session.kill()
		raise web.seeother("/")
		

class success(object):
	def GET(self):
		if session.username != "guest":
			return render.success(session.username)
		else:
			raise web.seeother("/login")