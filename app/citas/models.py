from datetime import datetime, time
from app import db


class Cita(db.Model):
    __tablename__ = "citas"

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    hora = db.Column(db.Time, nullable=False, default=lambda: time(9, 0))

    medico_id = db.Column(db.Integer, db.ForeignKey("medicos.id"), nullable=False)
    paciente_id = db.Column(db.Integer, db.ForeignKey("pacientes.id"), nullable=False)

    medico = db.relationship("Medico", back_populates="citas")
    paciente = db.relationship("Paciente", back_populates="citas")

    def __repr__(self):
        return f"<Cita {self.fecha} {self.hora} - Med:{self.medico_id} Pac:{self.paciente_id}>"