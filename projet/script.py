#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import textwrap
from dataclasses import dataclass
from datetime import datetime

random.seed()

@dataclass
class MicroUtopia:
    theme: str
    premise: str
    institution: str
    incentive: str
    constraint: str
    daily_scene: str
    failure_mode: str
    test: str
    questions: list[str]
    slogan: str
    name: str

THEMES = [
    "travail", "école", "démocratie", "IA", "ville", "énergie", "santé",
    "temps libre", "culture", "justice", "logement", "écologie", "innovation"
]

PREMISES = [
    "Toute décision publique doit être réversible et explicitement datée",
    "Le prestige social est attribué à l’utilité démontrée, pas au statut",
    "On ne rémunère plus l’effort mais l’impact vérifiable",
    "On limite volontairement l’optimisation pour préserver le vivant et le lien",
    "La vérité opérationnelle prime sur la vérité déclarative, preuves à l’appui",
    "La souveraineté appartient aux gens qui subissent les conséquences"
]

INSTITUTIONS = [
    "un Sénat des Conséquences composé d’habitants tirés au sort parmi les plus exposés",
    "une Banque du Temps qui prête des heures et facture des intérêts en attention",
    "un Tribunal des Promesses qui juge les organisations sur leurs engagements publics",
    "un Ministère des Bugs qui publie chaque semaine la liste des échecs et correctifs",
    "une Bourse des Externalités où l’on échange des droits d’impacter",
    "un Cadastre des Données où chaque donnée a un propriétaire, un prix et une durée"
]

INCENTIVES = [
    "un score public de fiabilité basé sur les prédictions tenues",
    "un dividende collectif versé quand un indicateur social progresse",
    "un système de crédits d’apprentissage échangeables contre des services",
    "des licences temporaires renouvelées seulement si l’impact est positif",
    "une réputation transférable, que tu peux perdre en cas de triche",
    "un bonus indexé sur la réduction de complexité, pas sur la croissance brute"
]

CONSTRAINTS = [
    "aucun algorithme ne peut être utilisé s’il n’explique pas son raisonnement en langage clair",
    "toute réforme doit inclure une clause de retour arrière avec conditions",
    "la publicité est interdite, seule l’information comparative est autorisée",
    "aucune organisation ne peut dépasser un seuil d’opacité comptable",
    "le droit à l’inaction est protégé par défaut, sauf rôle critique",
    "toute innovation doit déclarer ses perdants potentiels avant son lancement"
]

DAILY_SCENES = [
    "Au café, quelqu’un te propose d’échanger deux heures de ton temps contre une semaine de repas",
    "À l’école, les élèves notent la clarté des profs et la note a un effet sur le programme",
    "Dans un bus, un écran affiche les promesses tenues par la mairie ce trimestre",
    "Sur ton téléphone, tu vois le prix exact de l’impact carbone de ton achat, en euros",
    "À l’hôpital, l’IA doit justifier chaque recommandation en trois phrases compréhensibles",
    "Dans ton immeuble, un vote éclair décide d’un budget commun, traçable dépense par dépense"
]

FAILURE_MODES = [
    "les gens apprennent à jouer le système et à maximiser les métriques au détriment du sens",
    "une élite de spécialistes capture les règles et transforme la transparence en théâtre",
    "la société devient obsédée par la preuve, au point d’écraser l’intuition et l’art",
    "les effets secondaires se déplacent ailleurs et deviennent invisibles",
    "la vitesse de décision chute, et l’immobilisme se déguise en prudence",
    "la norme écrase les minorités d’usage et le système devient injuste par design"
]

TESTS = [
    "un pilote de 6 mois dans un quartier avec audit public hebdomadaire",
    "une expérimentation en entreprise sur 100 personnes avec mesure avant après",
    "un prototype numérique open source avec comité citoyen de contrôle",
    "un essai en université avec publication des données et droit de contestation",
    "une simulation multi agents où l’on cherche les stratégies de triche",
    "un A B test politique local où le groupe témoin garde les règles actuelles"
]

NAME_PARTS_A = ["Clair", "Nœud", "Tempo", "Agora", "Indice", "Boussole", "Sillage", "Contrat", "Essai", "Signal"]
NAME_PARTS_B = ["Civique", "Commun", "Réel", "Vivant", "Juste", "Prouvé", "Sobre", "Ouvert", "Responsable", "Apprenant"]

SLOGANS = [
    "Moins de promesses, plus de preuves",
    "La transparence qui fait mal, donc qui sert",
    "La confiance n’est pas un sentiment, c’est un protocole",
    "On ne réforme pas, on expérimente",
    "Le pouvoir suit les conséquences",
    "Rendre visible ce qui était gratuit, donc impuni"
]

QUESTION_TEMPLATES = [
    "Qui perd vraiment quand {x} devient la règle",
    "Quel est le moyen le plus simple de tricher avec {x}",
    "Quelle douleur quotidienne {x} rend-elle insupportable",
    "Quel acteur aura intérêt à saboter {x} en silence",
    "Quelle valeur humaine {x} risque-t-elle d’écraser",
    "Qu’est-ce que {x} rend impossible, et est-ce acceptable"
]

def pick(lst):
    return random.choice(lst)

def make_name():
    return f"{pick(NAME_PARTS_A)} {pick(NAME_PARTS_B)}"

def make_questions(core: str) -> list[str]:
    qs = random.sample(QUESTION_TEMPLATES, k=3)
    return [q.format(x=core.lower()) for q in qs]

def generate_micro_utopia(theme: str | None = None) -> MicroUtopia:
    t = theme.strip().lower() if theme else pick(THEMES)
    premise = pick(PREMISES)
    institution = pick(INSTITUTIONS)
    incentive = pick(INCENTIVES)
    constraint = pick(CONSTRAINTS)
    daily_scene = pick(DAILY_SCENES)
    failure_mode = pick(FAILURE_MODES)
    test = pick(TESTS)

    core = random.choice([premise, institution, incentive, constraint])
    questions = make_questions(core)
    slogan = pick(SLOGANS)
    name = make_name()

    return MicroUtopia(
        theme=t,
        premise=premise,
        institution=institution,
        incentive=incentive,
        constraint=constraint,
        daily_scene=daily_scene,
        failure_mode=failure_mode,
        test=test,
        questions=questions,
        slogan=slogan,
        name=name
    )

def format_micro_utopia(mu: MicroUtopia) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    blocks = [
        f"{mu.name}  micro utopie sur le thème : {mu.theme}",
        f"Horodatage : {now}",
        "",
        f"Principe fondateur : {mu.premise}",
        f"Institution clé : {mu.institution}",
        f"Incitation : {mu.incentive}",
        f"Contrainte non négociable : {mu.constraint}",
        "",
        f"Scène de vie : {mu.daily_scene}",
        f"Faille probable : {mu.failure_mode}",
        f"Test minimal : {mu.test}",
        "",
        f"Slogan : {mu.slogan}",
        "",
        "Questions qui piquent :",
        *[f"- {q} ?" for q in mu.questions],
    ]
    return "\n".join(textwrap.fill(b, width=92) if len(b) > 92 else b for b in blocks)

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Générateur de micro utopies, pour penser sans s’endormir.")
    parser.add_argument("--theme", type=str, default="", help="Ex: travail, démocratie, IA, école, ville...")
    parser.add_argument("--n", type=int, default=1, help="Nombre de propositions à générer")
    args = parser.parse_args()

    for i in range(args.n):
        mu = generate_micro_utopia(args.theme)
        print(format_micro_utopia(mu))
        if i < args.n - 1:
            print("\n" + "=" * 92 + "\n")

if __name__ == "__main__":
    main()
