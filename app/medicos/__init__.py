from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.medicos.models import Medico

bp_medicos = Blueprint("bp_medicos", __name__, template_folder="../templates/medicos")


@bp_medicos.route("/")
def index():
    medicos = Medico.query.all()
    return render_template("medicos/index.html", medicos=medicos)


@bp_medicos.route("/crear", methods=["GET", "POST"])
def crear():
    if request.method == "POST":
        db.session.add(Medico(
            nombre=request.form["nombre"],
            especialidad=request.form["especialidad"]
        ))
        db.session.commit()
        flash("Médico creado.", "success")
        return redirect(url_for("bp_medicos.index"))
    return render_template("medicos/form.html", medico=None)


@bp_medicos.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    medico = Medico.query.get_or_404(id)
    if request.method == "POST":
        medico.nombre = request.form["nombre"]
        medico.especialidad = request.form["especialidad"]
        db.session.commit()
        flash("Médico actualizado.", "success")
        return redirect(url_for("bp_medicos.index"))
    return render_template("medicos/form.html", medico=medico)


@bp_medicos.route("/eliminar/<int:id>", methods=["POST"])
def eliminar(id):
    medico = Medico.query.get_or_404(id)
    db.session.delete(medico)
    db.session.commit()
    flash("Médico eliminado.", "info")
    return redirect(url_for("bp_medicos.index"))