from flask_appbuilder import Model
from flask import Markup, url_for
from flask_appbuilder.filemanager import ImageManager
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from markupsafe import Markup
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.event import listens_for
from sqlalchemy.orm import relationship

from PropertyRegister.app import db


class Property(Model):
	id = Column(Integer, primary_key=True)
	name = Column(String(500), unique=True, nullable=False)
	popularity = Column(String(500))
	district = Column(String(500))
	address = Column(String(500))
	region = Column(String(500))
	area = Column(String(500))
	price = Column(String(500))
	unit = Column(String(500))
	availability = Column(String(500))
	photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

	def photo_img(self):
		im = ImageManager()
		if self.photo:
			return Markup('<a href="' + url_for('PropertyModelView.show', pk=str(self.id)) +
			              '" class="thumbnail"><img src="' + im.get_url(self.photo) +
			              '" alt="Photo" class="img-rounded img-responsive"></a>')
		else:
			return Markup('<a href="' + url_for('PropertyModelView.show', pk=str(self.id)) +
			              '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

	def photo_img_thumbnail(self):
		im = ImageManager()
		if self.photo:
			return Markup('<a href="' + url_for('PropertyModelView.show', pk=str(self.id)) +
			              '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
			              '" alt="Photo" class="img-rounded img-responsive"></a>')
		else:
			return Markup('<a href="' + url_for('PropertyModelView.show', pk=str(self.id)) +
			              '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

	def __repr__(self):
		return self.name


class Company(Model):
	id = Column(Integer, primary_key=True)
	name = Column(String(500), nullable=False)
	property_name = Column(String(500))
	room = Column(String(500))
	property_id = Column(Integer, ForeignKey('property.id'))
	property = relationship("Property")

	def __repr__(self):
		return self.name


@listens_for(Property.photo, 'modified')
def parse_image(target, initiator):
	stmt = Company.insert().values(name='test', propery_name='test', room='test', property_id='2615')
	db.session.execute(stmt)
	db.session.commit()
