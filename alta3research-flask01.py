#!/usr/bin/python
from flask import Flask
from flask import render_template
  
app = Flask(__name__)

@app.route('/')
def index():
  return jsonify(mutant_data)
mutant_data = {
         'name':'Magneto',
         'powers':['Magnetism','Intelligence','Charisma'],
         'roles':{
                 'Quiet Counsel':['Representative','Founder'],
                 'Brotherhood of Evil Mutants':['Patriarch', 'Founder']
          }
 }
@app.route('/multi' methods=['GET', 'POST'])
def multi():
  
  return render_template('index.html', player=mutant_data)
  
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=2224)
