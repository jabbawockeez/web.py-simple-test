import settings, web

session = web.ctx.session
render = settings.render

class index(object):
	def GET(self):
		try:
			username = session.username
		except AttributeError:
			username = "guest"
		return render.index(username)