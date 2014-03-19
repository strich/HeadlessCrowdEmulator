# Fix the div by 0 exception. Can also upgrade to Python 3.x:
from __future__ import division

from datetime import datetime, timedelta
from collections import Counter
import subprocess

class InputManager(object):
	buffered_input = []

	social_votes_anarchy = set('')
	social_votes_democracy = set('')

	last_social_type = "anarchy"

	anarchy_update_period = timedelta(milliseconds = 100)
	anarchy_update_next = datetime.now() + anarchy_update_period

	democracy_update_period = timedelta(seconds = 10)
	democracy_update_next = datetime.now() + democracy_update_period

	# How quickly we decay back towards anarchy:
	social_decay_period = timedelta(seconds = 1)
	social_decay_next = datetime.now() + social_decay_period

	@classmethod
	def add_social_vote(cls, social_type, userid):
		if social_type == "anarchy":
			cls.social_votes_democracy.discard(userid)
			cls.social_votes_anarchy.add(userid) 

		if social_type == "democracy":
			social_votes_anarchy.discard(userid)
			cls.social_votes_democracy.add(userid)

	@classmethod
	def get_social_type(cls):
		# Ensure we stay in democracy for at least one full period:
		if cls.democracy_update_next <= datetime.now() and cls.last_social_type == "democracy":
			return "democracy"

		if cls.get_social_anarchy_percentage() > 50:
			cls.last_social_type = "democracy"
			return "democracy"
		else:
			cls.last_social_type = "anarchy"
			return "anarchy"

	@classmethod
	def get_social_anarchy_percentage(cls):
		# Returns 0-100, 0 being completely anarchy.

		if len(cls.social_votes_democracy) == 0:
			return 0

		if len(cls.social_votes_anarchy) == 0 and len(cls.social_votes_democracy) == 0:
			return 0

		if len(cls.social_votes_anarchy) == 0 and len(cls.social_votes_democracy) != 0:
			return 1

		return len(cls.social_votes_democracy) / (len(cls.social_votes_democracy) + len(cls.social_votes_anarchy))

	@classmethod
	def update(cls):
		if cls.get_social_type() == "anarchy":
			if cls.anarchy_update_next <= datetime.now():
				#print "Sending input from anarchy"
				cls.send_input()
				cls.anarchy_update_next = datetime.now() + cls.anarchy_update_period

		if cls.get_social_type() == "democracy":
			if cls.democracy_update_next <= datetime.now():
				#print "Sending input from democracy"
				cls.send_input()
				cls.democracy_update_next = datetime.now() + cls.democracy_update_period

	@classmethod
	def add_input(cls, input_str):
		if input_str == "start":
			input_str = "Return"
                if input_str == "a":
                        input_str = "z"
                if input_str == "b":
                        input_str = "x"
                if input_str == "up":
                        input_str = "Up"
                if input_str == "down":
                        input_str = "Down"
                if input_str == "left":
                        input_str = "Left"
                if input_str == "right":
                        input_str = "Right"
		print(input_str)
		# TODO: Only allow certain strings through here
		cls.buffered_input.append(input_str)

		# Drop the oldest input if the buffer is over a certain size:
		if len(cls.buffered_input) > 50:
			cls.buffered_input.pop()

	@classmethod
	def get_input(cls):
		if len(cls.buffered_input) == 0:
			return # Nothing to send

		if cls.get_social_type() == "anarchy":
			key = cls.buffered_input.pop()

			#del cls.buffered_input[:] # Clear the list

			return key

		if cls.get_social_type() == "democracy":
			input_counter = Counter(cls.buffered_input)
			input_best = input_counter.most_common(1)
			input_best_str = input_best[0][0]
			input_best_count = input_best[0][1]

			del cls.buffered_input[:] # Clear the list

			return input_best_str

	@classmethod
	def send_input(cls):
		key = cls.get_input()

		if key is not None:
			subprocess.call(["xdotool", "search", "--class", "vbam", "key", "--delay", "100", key], env={"DISPLAY":":0"})

	@classmethod
	def decay_social(cls):
		if cls.social_decay_next <= datetime.now():
			cls.social_votes_anarchy.pop
			cls.social_decay_next = datetime.now() + cls.social_decay_period
