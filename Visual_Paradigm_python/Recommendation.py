#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Package import Student
from Package import Course
from typing import List

class Recommendation(object):
	def generateRecommendation(self):
		pass

	def __init__(self):
		self.___recommendationID : int = None
		self.___studentID : int = None
		self.___recommendedCourseID : int = None
		self._unnamed_Student_ : Student = None
		"""# @AssociationMultiplicity 1"""
		self._unnamed_Course_ : Course = None
		"""# @AssociationMultiplicity 1"""

