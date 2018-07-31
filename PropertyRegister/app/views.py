import json

from flask import render_template, redirect, flash
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, action
from PropertyRegister.app import db, appbuilder
from PropertyRegister.app.baidu_ocr import baidu_ocr
from .models import Property, Company


class CompanyModelView(ModelView):
	datamodel = SQLAInterface(Company)
	label_columns = {'property': 'Property'}
	# list_columns = ['photo_img_thumbnail', 'name', 'room']
	list_columns = ['name', 'room']
	show_fieldsets = [
		(
			'Summary',
			{'fields': ['name', 'room']}
		)]


class PropertyModelView(ModelView):
	datamodel = SQLAInterface(Property)
	list_columns = {'name': 'Name', 'district': 'District', 'address': 'Address', 'region': 'Region'}
	related_views = [CompanyModelView]

	def pre_update(self, item):
		property_id = item.id
		name = item.name
		if item.photo:
			image = item.photo
			ocr_res = baidu_ocr(image)
			for item in ocr_res:
				db.session.add(Company(name=item, property_name=name, room='', property_id=property_id))
				db.session.commit()
		# for prop in properties:
		flash('Company updated')

	# @action("capitalize", "Capitalize name", "Do you really want to capitalize the name?")
	# def capitalize(self, Property):
	# 	if isinstance(Property, list):
	# 		for prop in Property:
	# 			prop.name = prop.name.capitalize()
	# 			self.datamodel.edit(Property)
	# 			self.update_redirect()
	# 	else:
	# 		Property.name = Property.name.capitalize()
	# 		self.datamodel.edit(Property)
	# 	return redirect(self.get_redirect())


# @app.app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html', base_template=app.base_template, appbuilder=app), 404
#

db.create_all()
appbuilder.add_view(PropertyModelView, "List Properties", icon="fa-folder-open-o", category="Property", category_icon="fa-envelope")
appbuilder.add_view(CompanyModelView, "List Companies", icon="fa-folder-open-o", category="Property")
