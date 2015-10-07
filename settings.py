import web, main

web.config.debug = False

render = web.template.render("templates/", base = "base")