from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# ----------------------------------------------------------------------------#
# Models.
# ----------------------------------------------------------------------------#

Show = db.Table( 'Show', db.Column('id', db.Integer, primary_key=True),
        db.Column('venue_id', db.Integer, db.ForeignKey('Venue.id')),
        db.Column('artist_id', db.Integer, db.ForeignKey('Artist.id')),
        db.Column('start_time', db.DateTime, nullable=False))

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    webbsite = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(500))
    artists = db.relationship('Artist', secondary = Show, backref = db.backref('venues'))



class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    webbsite = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(500))
    venues = db.relationship('Venue', secondary = Show, backref = db.backref('artists'))

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

#class Show(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), primary_key= True)
#    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), primary_key= True)
#    start_time = db.Column(db.DateTime, nullable = False)


