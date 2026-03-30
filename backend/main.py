from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import random
import pathlib

app = FastAPI(title="Qui de nous ?", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

QUESTIONS = [
    "Qui est le plus susceptible de se perdre dans un IKEA ?",
    "Qui pourrait survivre le plus longtemps sur une ile deserte ?",
    "Qui est le plus susceptible de devenir celebre par accident ?",
    "Qui oublierait son propre anniversaire ?",
    "Qui est le plus susceptible de parler a son GPS ?",
    "Qui pourrait manger un repas entier sans lever les yeux de son telephone ?",
    "Qui serait le pire candidat de Koh-Lanta ?",
    "Qui est le plus susceptible de rire a un moment inapproprie ?",
    "Qui pourrait dormir n'importe ou, n'importe quand ?",
    "Qui est le plus susceptible d'envoyer un message a la mauvaise personne ?",
    "Qui pourrait regarder la meme serie 10 fois sans se lasser ?",
    "Qui est le plus susceptible de se tromper de porte en sortant des toilettes ?",
    "Qui survivrait le moins longtemps dans un film d'horreur ?",
    "Qui est le plus susceptible de pleurer devant un film Disney ?",
    "Qui serait le plus insupportable en road trip ?",
    "Qui est le plus susceptible de tomber amoureux d'un personnage fictif ?",
    "Qui pourrait accidentellement declencher une alarme incendie en cuisinant ?",
    "Qui est le plus susceptible de danser dans un ascenseur ?",
    "Qui serait le pire mentor pour un stagiaire ?",
    "Qui est le plus susceptible de commencer un regime le lundi et abandonner le mardi ?",
    "Qui pourrait passer une journee entiere a procrastiner et appeler ca de la reflexion ?",
    "Qui est le plus susceptible de repondre 'oui' sans avoir ecoute la question ?",
    "Qui est le plus susceptible d'avoir un fou rire pendant un moment de silence ?",
    "Qui pourrait perdre ses cles alors qu'elles sont dans sa main ?",
    "Qui est le plus susceptible de devenir ami avec un inconnu dans une file d'attente ?",
    "Qui serait le plus difficile a reveiller le matin ?",
    "Qui est le plus susceptible de faire un discours emu apres deux verres ?",
    "Qui pourrait survivre uniquement de pizza pendant un mois ?",
    "Qui est le plus susceptible de se filmer en train de tomber ?",
    "Qui serait le pire coequipier en escape game ?",
]

_used_indices: list[int] = []


@app.get("/api/question/random")
def get_random_question():
    global _used_indices
    if len(_used_indices) >= len(QUESTIONS):
        _used_indices = []
    available = [i for i in range(len(QUESTIONS)) if i not in _used_indices]
    idx = random.choice(available)
    _used_indices.append(idx)
    return {
        "question": QUESTIONS[idx],
        "remaining": len(QUESTIONS) - len(_used_indices),
        "total": len(QUESTIONS),
    }


@app.get("/api/question/reset")
def reset_questions():
    global _used_indices
    _used_indices = []
    return {"status": "reset", "total": len(QUESTIONS)}


@app.get("/api/health")
def health():
    return {"status": "ok"}


STATIC_DIR = pathlib.Path(__file__).parent / "static"

if STATIC_DIR.exists():
    app.mount("/assets", StaticFiles(directory=STATIC_DIR / "assets"), name="assets")

    @app.get("/{full_path:path}")
    def serve_spa(full_path: str):
        file_path = STATIC_DIR / full_path
        if file_path.is_file():
            return FileResponse(file_path)
        return FileResponse(STATIC_DIR / "index.html")
