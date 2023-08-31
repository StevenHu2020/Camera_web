from database import db


# articles
class Camera(db.Model):
    Name = db.Column(db.Text, primary_key=True)
    Brand = db.Column(db.Text, nullable=False)
    Type = db.Column(db.Text, nullable=False)
    ImageSensor = db.Column(db.Text, nullable=False)
    TotalPixels = db.Column(db.Integer, nullable=False)
    EffectivePixels = db.Column(db.Integer, nullable=False)
    ImageSize = db.Column(db.Text, nullable=False)
    FileFormats = db.Column(db.Text, nullable=False)
    FrameSizeAndFrameRate = db.Column(db.Text, nullable=False)
    FileFormatsMovie = db.Column(db.Text, nullable=False)
    ShutterSpeed = db.Column(db.Text, nullable=False)
    FrameAdvanceRate = db.Column(db.Integer, nullable=False)
    ISO = db.Column(db.Text, nullable=False)
    Dimensions = db.Column(db.Text, nullable=False)
    Weight = db.Column(db.Integer, nullable=False)
    Price = db.Column(db.Integer, nullable=False)
    Herf = db.Column(db.Text, nullable=False)
