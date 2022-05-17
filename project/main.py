
from flask import Blueprint,render_template,flash
from .forms import SimpleWebForm
from .models import Contacts,db

main = Blueprint("main", __name__, template_folder="templates", static_folder="static")

@main.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("404.html", error=e), 404

@main.route("/", methods=["GET", "POST"])
def homepage():
    form = SimpleWebForm()
    """
    homepage route
    """
    if form.validate_on_submit():
        
        existingEmail = db.session.query(Contacts).filter(
                Contacts.email == form.email.data
            ).first()
        
        if existingEmail is not None:
            flash ('This email already exists!','error')
            return render_template("homepage.html",form=form)

        Contact = Contacts(form.name.data,form.email.data)

        db.session.add(Contact)
        db.session.commit()
        flash ('Form submitted successfully','success')
        
    return render_template("homepage.html",form=form)

