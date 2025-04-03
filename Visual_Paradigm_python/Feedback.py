#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Package import Student
from Package import Teacher
from typing import List

class Feedback(object):
	def submitFeedback(self):
		pass

	def viewFeedback(self):
		pass

	def __init__(self):
		self.___feedbackID : int = None
		self.___studentID : int = None
		self.___teacherID : int = None
		self.___rating : int = None
		self.___comment : str = None
		self._unnamed_Student_ : Student = None
		"""# @AssociationMultiplicity 1"""
		self._unnamed_Teacher_ : Teacher = None
		"""# @AssociationMultiplicity 1"""

