from flask import Flask, render_template, request
from models.create import Creation
from models.view import View
app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'root'
# app.config['MYSQL_DB'] = 'recipe'



@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')
        
@app.route('/create', methods=['GET', 'POST'])
def create():
    #print('aaa', request.method)
    if request.method == 'POST':
        recipe = getRecipe()
        print(recipe)
        newCreation = Creation()
        newCreation.insert(recipe)
    return render_template('create.html')

def getRecipe():
    recipe = {}
    recipe['name'] = request.form.get('name')
    recipe['time'] = request.form.get('time')
    recipe['ing-name'] = request.form.get('ingredient')
    recipe['instructions'] = request.form.get('instruction')
    recipe['notes'] = request.form.get('notes')
    return recipe

@app.route('/view', methods=['GET', 'POST'])
def view():
    out = None
    finalOutput = ''
    print(request.method)
    if request.method == 'POST' :
        recipeName = request.form.get('name')
        v = View()
        out = v.fetch(recipeName)
        # print(out)
        time = out[0]
        ing = out[1]
        ins = out[2]
        notes = out[3]
        finalOutput = f'Recipe: {recipeName}\n Time: {time}\n Ingredients: {ing}\nInstructions: {ins}\nNotes: {notes}'
        out = finalOutput
        return render_template('view.html', output = out)

    return render_template('view.html', output = out)
if __name__ == '__main__':
    app.run(debug=True)


