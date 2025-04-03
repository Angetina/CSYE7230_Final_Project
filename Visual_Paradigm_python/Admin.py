#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Package import User
from typing import List

class Admin(User):
	def manageUsers(self):
		pass

	def generateReports(self):
		pass

	def __init__(self):
		self.___adminID : int = None
		self.___assignedCourses : str = None
		self._unnamed_Report_ = []
		"""# @AssociationMultiplicity 0..*"""

