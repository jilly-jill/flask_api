#!/usr/bin/python3
  2 from flask import Flask
  3 from flask import render_template
  4 
  5 
  6 app = Flask(__name__)
  7 
  8 
  9 @app.route('/')
 10 def index():
 11     return jsonify(mutant_data)
 12 
 13  mutant_data = {
 14         'name':'Magneto',
 15         'powers':['Magnetism','Intelligence','Charisma'],
 16         'roles':{
 17             'Quiet Counsel':['Representative','Founder'],
 18             'Brotherhood of Evil Mutants':['Patriarch', 'Founder']
