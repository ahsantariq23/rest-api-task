from flask import Flask
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)

class Home(Resource):
    def get(self,testData):
        return {"name":testData}

    
    
    
api.add_resource(Home,'/Home/<string:testData>')

if __name__=='__main__':
    app.run(debug=True)
