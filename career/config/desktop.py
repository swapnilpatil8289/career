# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Career",
                        "category": "Modules",
                        "label": _("Career"),
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
                        "description": "Job Application, Job Applicant, Job Opening."
		}
	]


