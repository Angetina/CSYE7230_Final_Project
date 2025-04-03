#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Package import Admin
from typing import List

class Report(object):
	def generateReport(self):
		pass

	def viewReport(self):
		pass

	def __init__(self):
		self.___reportID : int = None
		self.___generatedBy : int = None
		self.___date : str = None
		self._unnamed_Admin_ : Admin = None
		"""# @AssociationMultiplicity 1"""

