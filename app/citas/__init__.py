from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime
from app import db
from app.citas.models import Cita
from app.medicos.models import Medico
from app.pacientes.models import Paciente

bp_citas = Blueprint("bp_citas", __name__, template_folder="../templates/citas")


@bp_citas.route("/")
def index():
    citas = Cita.query.all()
    return render_template("citas/index.html", citas=citas)


@bp_citas.route("/crear", methods=["GET", "POST"])
def crear():
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()
    if request.method == "POST":
        db.session.add(Cita(
            fecha=datetime.strptime(request.form["fecha"], "%Y-%m-%d").date(),
            hora=datetime.strptime(request.form["hora"], "%H:%M").time(),
            medico_id=request.form["medico_id"],
            paciente_id=request.form["paciente_id"]
        ))
        db.session.commit()
        flash("Cita creada.", "success")
        return redirect(url_for("bp_citas.index"))
    return render_template("citas/form.html", cita=None, medicos=medicos, pacientes=pacientes)


@bp_citas.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    cita = Cita.query.get_or_404(id)
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()
    if request.method == "POST":
        cita.fecha = datetime.strptime(request.form["fecha"], "%Y-%m-%d").date()
        cita.hora = datetime.strptime(request.form["hora"], "%H:%M").time()
        cita.medico_id = request.form["medico_id"]
        cita.paciente_id = request.form["paciente_id"]
        db.session.commit()
        flash("Cita actualizada.", "success")
        return redirect(url_for("bp_citas.index"))
    return render_template("citas/form.html", cita=cita, medicos=medicos, pacientes=pacientes)


@bp_citas.route("/eliminar/<int:id>", methods=["POST"])
def eliminar(id):
    cita = Cita.query.get_or_404(id)
    db.session.delete(cita)
    db.session.commit()
    flash("Cita eliminada.", "info")
    return redirect(url_for("bp_citas.index"))