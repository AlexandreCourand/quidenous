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
    "Qui est le plus susceptible de gouter un truc bizarre juste par curiosite ?",
    "Qui pourrait oublier pourquoi il est entre dans une piece ?",
    "Qui est le plus susceptible de chanter sous la douche a plein volume ?",
    "Qui serait le premier a craquer pendant un concours de silence ?",
    "Qui est le plus susceptible d'adopter un animal sur un coup de tete ?",
    "Qui pourrait porter le meme pyjama trois jours de suite sans culpabiliser ?",
    "Qui est le plus susceptible de raconter la fin d'un film sans prevenir ?",
    "Qui serait le plus nul pour monter un meuble en kit ?",
    "Qui est le plus susceptible de faire semblant de connaitre une chanson en soiree ?",
    "Qui pourrait manger un dessert avant le plat principal ?",
    "Qui est le plus susceptible de se faire arnaquer par un vendeur trop sympa ?",
    "Qui serait le dernier a quitter la piste de danse ?",
    "Qui est le plus susceptible de confondre sel et sucre en cuisinant ?",
    "Qui pourrait porter des chaussettes depareillees sans s'en rendre compte ?",
    "Qui est le plus susceptible de stalker quelqu'un sur les reseaux pendant 2 heures ?",
    "Qui serait le plus mauvais joueur au Monopoly ?",
    "Qui est le plus susceptible de rater son arret de bus en revassant ?",
    "Qui pourrait tenir une conversation entiere avec un chat ?",
    "Qui est le plus susceptible de se bruler en sortant un plat du four ?",
    "Qui serait le pire gardien de secret du groupe ?",
    "Qui est le plus susceptible de faire un achat impulsif a 3h du matin ?",
    "Qui pourrait survivre sans internet pendant une semaine ?",
    "Qui est le plus susceptible de pleurer en ecoutant une chanson triste ?",
    "Qui serait le plus flippant deguise en clown ?",
    "Qui est le plus susceptible de liker une photo de 2015 par accident ?",
    "Qui pourrait manger piquant sans broncher ?",
    "Qui est le plus susceptible de parler tout seul dans la rue ?",
    "Qui serait le plus insupportable en tant que prof ?",
    "Qui est le plus susceptible de se reveiller avec la trace de l'oreiller sur la joue ?",
    "Qui pourrait regarder un film d'horreur sans sursauter une seule fois ?",
    "Qui est le plus susceptible de se tromper de prenom en appelant quelqu'un ?",
    "Qui serait le plus dangereux au volant d'un caddie de supermarche ?",
    "Qui est le plus susceptible de faire un malaise en voyant du sang ?",
    "Qui pourrait manger la meme chose tous les jours pendant un mois ?",
    "Qui est le plus susceptible de se cacher derriere le canape pendant un orage ?",
    "Qui serait le pire baby-sitter ?",
    "Qui est le plus susceptible d'arriver en retard a son propre mariage ?",
    "Qui pourrait negocier le prix d'un truc qui n'est pas negociable ?",
    "Qui est le plus susceptible de faire une sieste pendant une reunion ?",
    "Qui serait le premier a appeler au secours dans une maison hantee ?",
    "Qui est le plus susceptible de dire 'je suis pas fatigue' et s'endormir 5 minutes apres ?",
    "Qui pourrait vivre dans un van amenage sans probleme ?",
    "Qui est le plus susceptible de photographier son repas avant de manger ?",
    "Qui serait le pire DJ en soiree ?",
    "Qui est le plus susceptible de trébucher sur un sol parfaitement plat ?",
    "Qui pourrait manger un kebab a 8h du matin ?",
    "Qui est le plus susceptible de se plaindre du froid en ete ?",
    "Qui serait le plus relou en avion ?",
    "Qui est le plus susceptible d'avoir toujours un snack dans son sac ?",
    "Qui pourrait confondre sa gauche et sa droite sous pression ?",
    "Qui est le plus susceptible de tomber en marchant et de dire 'c'est rien' ?",
    "Qui serait le plus dramatique pour un petit bobo ?",
    "Qui est le plus susceptible d'oublier le code de sa carte bleue ?",
    "Qui pourrait faire croire n'importe quoi a n'importe qui ?",
    "Qui est le plus susceptible de se retrouver dans une situation absurde un mardi apres-midi ?",
    "Qui serait le plus flippant si on le croisait la nuit ?",
    "Qui est le plus susceptible de garder un emballage vide dans son sac pendant des semaines ?",
    "Qui pourrait commander le plat le plus cher du menu sans hesiter ?",
    "Qui est le plus susceptible de ronfler en public ?",
    "Qui serait le pire colocataire ?",
    "Qui est le plus susceptible de se battre pour la derniere part de gateau ?",
    "Qui pourrait apprendre une choregraphie TikTok en une heure ?",
    "Qui est le plus susceptible de raconter une blague et rire avant la chute ?",
    "Qui serait le plus convaincant en tant que politicien ?",
    "Qui est le plus susceptible de mettre du ketchup sur tout ?",
    "Qui pourrait rester zen dans un embouteillage de 3 heures ?",
    "Qui est le plus susceptible de faire un speech improvise devant des inconnus ?",
    "Qui serait le plus nul pour garder une plante en vie ?",
    "Qui est le plus susceptible de s'inscrire a un marathon sans jamais s'entrainer ?",
    "Qui pourrait repondre a un mail pro un dimanche a 23h ?",
    "Qui est le plus susceptible de se mettre a pleurer devant un coucher de soleil ?",
    "Qui serait le plus drole en stand-up comedy ?",
    "Qui est le plus susceptible de faire un roadtrip sans carte ni GPS ?",
    "Qui pourrait manger des cereales a minuit comme repas principal ?",
    "Qui est le plus susceptible de se porter volontaire pour un truc sans savoir ce que c'est ?",
    "Qui serait le plus intense dans un karaoke ?",
    "Qui est le plus susceptible de perdre son telephone dans le frigo ?",
    "Qui pourrait passer un week-end entier sans parler a personne et etre heureux ?",
    "Qui est le plus susceptible de faire un compliment tellement bizarre que ca met mal a l'aise ?",
    "Qui serait le dernier a comprendre une blague ?",
    "Qui est le plus susceptible de porter des lunettes de soleil quand il pleut ?",
    "Qui pourrait manger un plat trop sale sans rien dire pour ne pas vexer le cuisinier ?",
    "Qui est le plus susceptible de se perdre dans sa propre ville ?",
    "Qui serait le pire candidat de MasterChef ?",
    "Qui est le plus susceptible de danser seul dans sa cuisine ?",
    "Qui pourrait dormir avec 15 alarmes et quand meme etre en retard ?",
    "Qui est le plus susceptible de creer un groupe WhatsApp inutile ?",
    "Qui serait le plus effrayant en tant que patron ?",
    "Qui est le plus susceptible de relire ses propres messages et de regretter ?",
    "Qui pourrait faire du sport en tongs ?",
    "Qui est le plus susceptible de commander un Uber pour faire 500 metres ?",
    "Qui serait le plus susceptible de devenir un influenceur LinkedIn ?",
    "Qui est le plus susceptible de ramener un souvenir kitsch de chaque voyage ?",
    "Qui pourrait faire croire qu'il est malade pour eviter un truc ?",
    "Qui est le plus susceptible d'appuyer sur 'repondre a tous' par accident ?",
    "Qui serait le plus dur a battre au bras de fer ?",
    "Qui est le plus susceptible de pleurer devant une pub ?",
    "Qui pourrait sortir de chez lui en pantoufles sans s'en apercevoir ?",
    "Qui est le plus susceptible de se lancer dans un debat passionne sur un sujet qu'il ne maitrise pas ?",
    "Qui pourrait oublier qu'il a deja raconte la meme histoire trois fois ?",
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
