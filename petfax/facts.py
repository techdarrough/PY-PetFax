from flask import Blueprint, redirect, render_template, request 




bp = Blueprint('facts', __name__, url_prefix="/facts")

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        return redirect('/facts')
    return render_template('facts/index.html')

 
@bp.route('/new')
def new(): 
    return render_template('facts/new.html')