from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.pacientes.models import Paciente

bp_pacientes = Blueprint("bp_pacientes", __name__, template_folder="../templates/pacientes")


@bp_pacientes.route("/")
def index():
    pacientes = Paciente.query.all()
    return render_template("pacientes/index.html", pacientes=pacientes)


@bp_pacientes.route("/crear", methods=["GET", "POST"])
def crear():
    if request.method == "POST":
        db.session.add(Paciente(
            nombre=request.form["nombre"],
            telefono=request.form["telefono"]
        ))
        db.session.commit()
        flash("Paciente creado.", "success")
        return redirect(url_for("bp_pacientes.index"))
    return render_template("pacientes/form.html", paciente=None)


@bp_pacientes.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    paciente = Paciente.query.get_or_404(id)
    if request.method == "POST":
        paciente.nombre = request.form["nombre"]
        paciente.telefono = request.form["telefono"]
        db.session.commit()
        flash("Paciente actualizado.", "success")
        return redirect(url_for("bp_pacientes.index"))
    return render_template("pacientes/form.html", paciente=paciente)


@bp_pacientes.route("/eliminar/<int:id>", methods=["POST"])
def eliminar(id):
    paciente = Paciente.query.get_or_404(id)
    db.session.delete(paciente)
    db.session.commit()
    flash("Paciente eliminado.", "info")
    return redirect(url_for("bp_pacientes.index"))