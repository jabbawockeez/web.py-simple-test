import settings, main

#session = web.ctx.session
session = main.session
render = settings.render

class index(object):
	def GET(self):
		'''
		try:
			username = session.username
		except AttributeError:
			username = "guest"
		'''

		username = session.__getitem__('username') or "guest"

		return render.index(username)