import json
import random
from flask import Flask,request, jsonify, render_template



app = Flask(__name__)

#json data 
mutate =[{"alias": "Magneto",
    "image": 'https://static2.cbrimages.com/wordpress/wp-content/uploads/2019/12/Magneto.jpg',         
    "name": "Erik Leshner",
    "location": "Krakoa",
    "powers": ["Magnetism Manipulation", "Flight", "Telepathic Defense"],
    "quotes": [
        "So… in effect, you swapped 5,000 human lives for one mutant one. That’s regrettable. But when there’s less than 200 mutants on the planet, I can live with that.",
        "The thing none of you will ever understand is that there are no sides. There are no heroes or villains. There’s just what I want and how I’ll get it."]
},
{"alias": "Legion",
    "image": 'https://screenrant.com/wp-content/uploads/legion-x-men-comics-tv-show.jpg', 
    "name": "David Heller",
    "location": "Krakoa",
    "powers": ["Reality Manipulation", "Telekinesis", "Telepathy", "Teleportation"],
     "quotes": [
        "I have come far for you Erik Magnus Lehnsherr! In my tomorrow, you will become the greatest villain the world has ever known! And for that, you must die -- today!",
       "Don't try to stop me, Ororo. Applaud me."]
},
{"alias": "Storm",
    "image": 'https://static0.cbrimages.com/wordpress/wp-content/uploads/2020/04/Storm-Header-Cropped.jpg', 
    "name": "Ororo Munroe",
    "location": "Krakoa",
    "powers": ["Weather Manipulation", "Flight", "Lightning Immunity", "Tactician"],
    "quotes": [
        "You spoke once of power. Little man, you do not know the meaning of the word!",
        "Am I not beautiful, Lord Doom? And terrible? Do you not fear me? You should."]
},
{"alias": "Rogue",
    "image": 'https://imgix.ranker.com/user_node_img/50012/1000221170/original/rogue-in-green-and-yellow-suit-with-trench-coat-photo-u1?fit=crop&fm=pjpg&q=60&w=650&dpr=2', 
    "name": "Anne Marie LeBeau",
    "location": "Krakoa",
    "powers": ["Life force absorption", "Flight", "Durability"],
    "quotes": ["That's why we do it, Joseph. For the innocents, the ones who ain't been taught t' hate yet. Our hope for tomorrow. Change is gonna come...",
               "Ah'm giving you one last chance to surrender, sugah. After that, it could get ugly."]
    },
{"alias": "Gambit",
    "image": 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/6d95a130-762b-4c0c-a634-0eca8c409a79/d3ghdzn-e818840e-a90d-4b51-876f-b38968b828fa.png/v1/fill/w_752,h_1063,q_75,strp/gambit_from_x_men_by_lonelindarts-d3ghdzn.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwic3ViIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl0sIm9iaiI6W1t7InBhdGgiOiIvZi82ZDk1YTEzMC03NjJiLTRjMGMtYTYzNC0wZWNhOGM0MDlhNzkvZDNnaGR6bi1lODE4ODQwZS1hOTBkLTRiNTEtODc2Zi1iMzg5NjhiODI4ZmEucG5nIiwid2lkdGgiOiI8PTc1MiIsImhlaWdodCI6Ijw9MTA2MyJ9XV19._AWucK0bWnXa8osmXogXRcYASNYGefHmDINexSXUWGs', 
    "name": "Remy LeBeau",
    "location": "Krakoa",
    "powers": ["Kinetic Energy Generation", "Kinetic Energy Manipulation", "Charisma"],
    "quotes": ["I honestly cannot remember the last time we caught a break.",
               "The gentleman assumes the pot is his to win... but I have a literal ace up my sleeve."]
    },
{"alias": "Bishop",
    "image": 'https://i.pinimg.com/736x/f2/dd/64/f2dd6473df371ea5976ca048af48bbb7.jpg', 
    "name": "Erik Leshner",
    "location": "Krakoa",
    "powers": ["Energy Absorption", "Energy Redirection", "Superhuman Physical Abilities", "Instinct"],
    "quotes": ["If you plan on leaving, don't plan on doing it alive.",
               " If you let rage and hate over what happened define your life... then inside, in your heart and soul, you'll find yourself just as dead."]}
]
# get/post json data
@app.route("/data", methods = ["GET", "POST"])
def index():
    if request.method == 'POST':
        data = request.json
        if data:
            data = json.loads(data)
            alias = data["alias"]
            name = data["name"]
            powers = data["powers"]
            quotes = data["quotes"]
            image = data["image"]
            mutate.append({"alias":alias,"name": name,"powers": powers,"quotes":quotes,"image":image})
    return jsonify(mutate)
    
# welcome and / == same location 
@app.route("/")
@app.route("/welcome")
def greet():
    # generate random xmen alias for img/quote generation
    mut=random.choice(mutate)
    mutant = mut.get('alias')
    mut_q = mut.get('quotes')
    image_mutant = mut.get('image')
    # generate random number for quote 1 or 2 
    qt_ran = random.randrange(0, 1)
    quote_mutant = mut_q[qt_ran]
    #format img to html 
    mut_image = f"<img id='char_img' src=\"{image_mutant}\"></img>"
    # when button is clicked - links to mutants page 
    return render_template("index.html",
                             mutant=mutant, mut_image=mut_image, quote_mutant=quote_mutant)
    
@app.route("/mutants")
def mutant_ask():
     # generate random xmen alias for img/quote generation
    mut=random.choice(mutate)
    mutant = mut.get('alias')
    mut_q = mut.get('quotes')
    image_mutant = mut.get('image')
    # generate random number for quote 1 or 2 
    qt_ran = random.randrange(0, 1)
    quote_mutant = mut_q[qt_ran]
    print(image_mutant)
    #format img to html 
    mut_image = f"<img id='char_img' src=\"{image_mutant}\"></img>"
    # when button is clicked - links to mutants page 
    return render_template("mutants.html", mutant = mutant, mut_image=mut_image, quote_mutant=quote_mutant)



if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 2224)
