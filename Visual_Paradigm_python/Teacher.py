#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Package import User
from typing import List

class Teacher(User):
	def createCourse(self):
		pass

	def updateSchedule(self):
		pass

	def checkFeedback(self):
		pass

	def __init__(self):
		self.___teacherID : int = None
		self.___specialty : str = None
		self.___salary : float = None
		self.___assignedCourses : str = None
		self._unnamed_Feedback_ = []
		"""# @AssociationMultiplicity 1..*"""
		self._unnamed_Course_ = []
		"""# @AssociationMultiplicity 1..*"""

