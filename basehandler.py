import os, sys


class BaseHandler:

	handler_version = "1.0.0"
	description = ""
	options = []

	def get_filename(self):
		return os.path.basename(sys.modules[self.__module__].__file__)

	def attach_arguments(self, argparser):
		pass

	def get_update(self, smarthash_version):
		return ""

	def check_parameters(self, args):
		pass

	def early_validation(self, path, data):
		pass

	def handle(self, data):
		pass