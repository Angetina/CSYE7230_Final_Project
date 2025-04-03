#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Package import Teacher
from Package import Schedule
from typing import List

class Course(object):
	def getCourseInfo(self):
		pass

	def updateCourse(self):
		pass

	def __init__(self):
		self.___courseID : int = None
		self.___title : str = None
		self.___duration : int = None
		self.___difficulty : str = None
		self.___teacherID : int = None
		self.___remainingSeats : int = None
		self.___startDate : str = None
		self.___courseStatus : str = None
		self._unnamed_Enrollment_ = []
		"""# @AssociationMultiplicity 1..*"""
		self._unnamed_Teacher_ : Teacher = None
		"""# @AssociationMultiplicity 1"""
		self._unnamed_LearningProgress_ = []
		"""# @AssociationMultiplicity 0..*"""
		self._unnamed_Recommendation_ = []
		"""# @AssociationMultiplicity 0..*"""
		self._unnamed_Schedule_ : Schedule = None
		"""# @AssociationKind Composition"""

