#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Package import Student
from typing import List

class Payment(object):
	def processPayment(self):
		pass

	def refundPayment(self):
		pass

	def __init__(self):
		self.___paymentID : int = None
		self.___studentID : int = None
		self.___amount : float = None
		self.___date : str = None
		self.___paymentMethod : str = None
		self.___paymentStatus : str = None
		self._unnamed_Student_ : Student = None
		"""# @AssociationMultiplicity 1"""
		self._unnamed_Enrollment_ = []
		"""# @AssociationMultiplicity 1..*"""

