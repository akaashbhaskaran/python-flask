from flask import Flask,request
import requests

def create_app():
	app = Flask(__name__)

	@app.route('/')
	def sort():

		endpoints = ['https://raw.githubusercontent.com/assignment132/assignment/main/duckduckgo.json','https://raw.githubusercontent.com/assignment132/assignment/main/google.json','https://raw.githubusercontent.com/assignment132/assignment/main/wikipedia.json']
	
		if 'sortKey' not in request.args or 'limit' not in request.args:
			return 'Input params missing' , 400 
		sortKey = request.args.get('sortKey')
		limit = int(request.args.get('limit'))
		data = []
		for url in endpoints:
			r = requests.get(url)
		
			if r.status_code == 200:
				data.extend(r.json()['data'])
		
		if sortKey not in data[0]:
			return 'Invalid Sort Key', 400
		data = sorted(data, key=lambda item: item[sortKey], reverse=False)
	
		return {'data':data[0:limit],'count':limit}

	return app
# main driver function
if __name__ == '__main__':
	app = create_app()
	app.run()

