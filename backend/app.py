from flask import Flask,request
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from decouple import config


name=config('name')
password=config('password')
database=config('database')



app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']=f'postgresql://{name}:{password}@localhost/{database}'


api = Api(app)

db = SQLAlchemy(app)


# model for response marshalling
color_model = api.model("Color", {"color": fields.String, "hex": fields.String})


# database model
class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(10), nullable=False)
    hex = db.Column(db.String(10), nullable=False)

    def __init__(self, color, hex):
        self.color = color
        self.hex = hex

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def create(cls, color, hex):
        new_color = cls(color=color, hex=hex)

        new_color.save()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)

    def delete(self):
        db.session.delete(self)
        db.session.commit()


@api.route("/")
class Hello(Resource):
    def get(self):
        pass


@api.route("/colors")
class Colors(Resource):
    
    @api.marshal_list_with(color_model,envelope='colors')
    def get(self):
        colors =Color.query.all()
        return colors

    @api.marshal_list_with(color_model,envelope='colors')
    def post(self):
        data=request.get_json()

        color=data.get('color')

        color_hex=data.get('hex')

        new_color=Color(color=color,hex=color_hex)

        new_color.save()
        
        return new_color


@api.route('/color/<int:id>')
class ColorResource(Resource):

    @api.marshal_with(color_model,envelope='color')
    def get(self,id):
        color=Color.query.get_or_404(id)

        return color

@app.shell_context_processor
def make_shell_context():
    return {
        "app":app,
        "db":db,
        "Color":Color,
    }

if __name__ == "__main__":
    app.run(debug=True)
