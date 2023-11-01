import webpy

def handler(app: webpy.App, *args):
	from flask import Response
	
	return Response(status=404)
