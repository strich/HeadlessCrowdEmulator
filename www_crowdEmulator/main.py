import tornado.ioloop
import tornado.web
import os.path
from InputManager import *

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html")
		#self.write("Hello, world")
		#InputManager.add_input("A")
		#InputManager.add_input("B")
		#InputManager.add_input("C")

		#self.write("Next Input: " + str(InputManager.get_input()) + "<br>")
		#self.write("Percent towards democracy: " + str(InputManager.get_social_anarchy_percentage()) + "<br>")
		#self.write("All buffered input: " + str(InputManager.buffered_input) + "<br>")
		#self.write("Next Input: " + str(InputManager.get_input()) + "<br>")
		#self.write("Next Input: " + str(InputManager.get_input()) + "<br>")

class AdminPanelHandler(tornado.web.RequestHandler):
	def get(self):
		#self.write("Next Input: " + str(InputManager.get_input()) + "<br>")
		self.write("Percent towards democracy: " + str(InputManager.get_social_anarchy_percentage()) + "<br>")
		self.write("All buffered input: " + str(InputManager.buffered_input) + "<br>")
		#self.write("Next Input: " + str(InputManager.get_input()) + "<br>")
		#self.write("Next Input: " + str(InputManager.get_input()) + "<br>")	

class InputHandler(tornado.web.RequestHandler):
	def post(self):
		input_str = self.get_argument('input', '')
		userid = self.get_argument('userid', '')
		self.write("Got input of " + input_str + " from user " + userid)
		InputManager.add_input(input_str)

application = tornado.web.Application(
	[
		(r"/", MainHandler),
		(r"/input", InputHandler),
		(r"/admin_panel", AdminPanelHandler)
	],
	template_path=os.path.join(os.path.dirname(__file__), "templates"),
	static_path=os.path.join(os.path.dirname(__file__), "static")
	)

if __name__ == "__main__":
	application.listen(80)
	#callback=lambda: 
	main_loop = tornado.ioloop.IOLoop.instance()
	inputmanager_update = tornado.ioloop.PeriodicCallback(InputManager.update, 10, main_loop)
	inputmanager_update.start()
	main_loop.start()
