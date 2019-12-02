from flask_sqlalchemy import SQLAlchemy

import json
from collections import namedtuple

db = SQLAlchemy()

# ----------------------------------------------------------------------------#
# Models.
# ----------------------------------------------------------------------------#

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
    website = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String(40)))
    seeking_talent = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(500))
    shows = db.relationship('Show', backref='venue', cascade='all, delete-orphan' , lazy=True)


    def seed_data(self):
        Venue.query.delete()

        data1 = {
            "name": "The Musical Hop",
            "genres": ["Jazz", "Reggae", "Swing", "Classical", "Folk"],

            "address": "1015 Folsom Street",
            "city": "San Francisco",
            "state": "CA",
            "phone": "123-123-1234",
            "website": "https://www.themusicalhop.com",
            "facebook_link": "https://www.facebook.com/TheMusicalHop",
            "seeking_talent": True,
            "seeking_description": "We are on the lookout for a local artist to play every two weeks. Please call us.",
            "image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60"
        }
        data2 = {
            "name": "The Dueling Pianos Bar",
            "genres": ["Classical", "R&B", "Hip-Hop"],
            "address": "335 Delancey Street",
            "city": "New York",
            "state": "NY",
            "phone": "914-003-1132",
            "website": "https://www.theduelingpianos.com",
            "facebook_link": "https://www.facebook.com/theduelingpianos",
            "seeking_talent": False,
            "image_link": "https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80"
        }
        data3 = {
            "name": "Park Square Live Music & Coffee",
            "genres": ["Rock n Roll", "Jazz", "Classical", "Folk"],
            "address": "34 Whiskey Moore Ave",
            "city": "San Francisco",
            "state": "CA",
            "phone": "415-000-1234",
            "website": "https://www.parksquarelivemusicandcoffee.com",
            "facebook_link": "https://www.facebook.com/ParkSquareLiveMusicAndCoffee",
            "seeking_talent": False,
            "image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80"
        }

        venues = [data1,data2,data3]

        for data in venues:
            venue = Venue(**data)
            db.session.add(venue)

        db.session.commit()


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String(40)))
    seeking_venue = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(500))
    shows = db.relationship('Show', backref='artist', lazy=True)


    def seed_data(self):
        Artist.query.delete()

        data1 = {
            "name": "Guns N Petals",
            "genres": ["Rock n Roll"],
            "city": "San Francisco",
            "state": "CA",
            "phone": "326-123-5000",
            "website": "https://www.gunsnpetalsband.com",
            "facebook_link": "https://www.facebook.com/GunsNPetals",
            "seeking_venue": True,
            "seeking_description": "Looking for shows to perform at in the San Francisco Bay Area!",
            "image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80"
        }
        data2 = {
            "name": "Matt Quevedo",
            "genres": ["Jazz"],
            "city": "New York",
            "state": "NY",
            "phone": "300-400-5000",
            "facebook_link": "https://www.facebook.com/mattquevedo923251523",
            "seeking_venue": False,
            "image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80"

        }
        data3 = {
            "name": "The Wild Sax Band",
            "genres": ["Jazz", "Classical"],
            "city": "San Francisco",
            "state": "CA",
            "phone": "432-325-5432",
            "seeking_venue": False,
            "image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80"
        }

        artists = [data1,data2,data3]

        for data in artists:
            artist = Artist(**data)
            db.session.add(artist)

        db.session.commit()

class Show(db.Model):
    __tablename__ = 'Show'
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), primary_key= True)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), primary_key= True)
    start_time = db.Column(db.String(50), nullable = False)

    def __repr__(self):
        return f'<Show ID: {self.venue_id} Artist_ID: {self.artist_id} Venue_ID: {self.venue_id} Start_time: {self.start_time} ' \
               f'Image: {self.artist.image_link} >'

    def seed_data(self):
        Show.query.delete()

        data = [{
            "venue_id": 1,
            "artist_id": 1,
            "start_time": "2019-05-21T21:30:00.000Z"
        }, {
            "venue_id": 3,
            "artist_id": 2,
            "start_time": "2019-06-15T23:00:00.000Z"
        }, {
            "venue_id": 3,
            "artist_id": 3,
            "start_time": "2035-04-01T20:00:00.000Z"
        }, {
            "venue_id": 3,
            "artist_id": 1,
            "start_time": "2035-04-08T20:00:00.000Z"
        }, {
            "venue_id": 2,
            "artist_id": 3,
            "start_time": "2035-04-15T20:00:00.000Z"
        }]

        for show in data:
            show = Show(**show)
            db.session.add(show)

        db.session.commit()
