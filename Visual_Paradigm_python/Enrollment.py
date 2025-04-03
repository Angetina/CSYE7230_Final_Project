#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Package import Payment
from Package import Student
from Package import Course
from typing import List

class Enrollment(object):
	def confirmEnrollment(self):
		pass

	def cancelEnrollment(self):
		pass

	def setUnnamed_Student_(self, aUnnamed_Student_ : Student) -> None:
		self._unnamed_Student_ = aUnnamed_Student_

	def getUnnamed_Student_(self) -> Student:
		return self._unnamed_Student_

	def setUnnamed_Course_(self, aUnnamed_Course_ : Course) -> None:
		self._unnamed_Course_ = aUnnamed_Course_

	def getUnnamed_Course_(self) -> Course:
		return self._unnamed_Course_

	def __init__(self):
		self.___enrollmentID : int = None
		self.___studentID : int = None
		self.___courseID : int = None
		self.___status : str = None
		self._unnamed_Payment_ : Payment = None
		"""# @AssociationMultiplicity 1"""
		self._unnamed_Student_ : Student = None
		"""# @AssociationType Package.Student
		# @AssociationMultiplicity 1..*"""
		self._unnamed_Course_ : Course = None
		"""# @AssociationType Package.Course
		# @AssociationMultiplicity 1..*"""

