#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web, url, settings, mysession

web.config.debug = True

app = web.application(url.urls, globals())

session = mysession.MemCacheStore()
session.__setitem__('username', "guest")
#session = web.session.Session(app, MemCacheStore(), {"username" : "guest", "password" : ""})
#session = web.session.Session(app, web.session.DiskStore('sessions'), {"username" : "guest", "password" : ""})
"""if web.config.get("_session") is None:
	session = web.session.Session(app, web.session.DiskStore('sessions'), {"username" : "guest", "password" : ""})
	web.config._session = session
else:
	session = web.config.get("_session")"""

'''
def session_hook():
	web.ctx.session = session

app.add_processor(web.loadhook(session_hook))
'''

if __name__ == '__main__':
	app.run()