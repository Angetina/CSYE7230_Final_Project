#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Package import User
from typing import List

class Student(User):
	def enrollCourse(self):
		pass

	def viewSchedule(self):
		pass

	def giveFeedback(self):
		pass

	def __init__(self):
		self.___studentID : int = None
		self.___membershipType : str = None
		self.___accountBalance : float = None
		self.___paymentStatus : str = None
		self.___isLoggedIn : long = None
		self.___registrationStatus : str = None
		self._unnamed_Recommendation_ = []
		"""# @AssociationMultiplicity 0..*"""
		self._unnamed_Enrollment_ = []
		"""# @AssociationMultiplicity 1..*"""
		self._unnamed_Payment_ = []
		"""# @AssociationMultiplicity 1..*"""
		self._unnamed_Feedback_ = []
		"""# @AssociationMultiplicity 1..*"""
		self._unnamed_LearningProgress_ = []
		"""# @AssociationMultiplicity 0..*"""

