# -*- coding: utf-8 -*-
"""lichess-api-requests.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16bGybi3jm1-6wSLzj0bFon_r3RPAGbov
"""

import pandas as pd
import requests

variantes = ["ultraBullet", "bullet", "blitz", "rapid", "classical", "chess960", "crazyhouse", "antichess", "atomic", "horde", "kingOfTheHill", "racingKings", "threeCheck"]

jugador = {
  "id_jugador": [],
  "nombre": [],
  "horas_jugadas": [],
  "titulo": [],

}

modo_de_juego = {
  "id_jugador": [],
  "nombre": [],
  "cantidad_partidas": [],
  "rating": []
}


for variante in variantes:
  respuesta = requests.get("https://lichess.org/api/player/top/10/" + variante)
  usuarios = respuesta.json()
  for usuario in usuarios["users"]:
    nombre = usuario["username"]
    respuesta = requests.get("https://lichess.org/api/user/" + nombre)
    estadisticas = respuesta.json()

    jugador["id_jugador"].append(estadisticas["id"])
    jugador["nombre"].append(estadisticas["username"])
    jugador["horas_jugadas"].append(estadisticas["playTime"]["total"]/60/60)
    if "title" in estadisticas: jugador["titulo"].append(estadisticas["title"])
    else: jugador["titulo"].append("-")

    for key, value in estadisticas["perfs"].items():
      if key != "storm" and key != "racer" and key != "streak":
        modo_de_juego["id_jugador"].append(estadisticas["id"])
        modo_de_juego["nombre"].append(key)
        modo_de_juego["cantidad_partidas"].append(value["games"])
        modo_de_juego["rating"].append(value["rating"])

jugadores = pd.DataFrame(jugador)
modosDeJuego = pd.DataFrame(modoDeJuego)
jugadores.to_csv("../csv/jugadores-lichess.csv")
modosDeJuego.to_csv("../csv/estadisticas-modos-de-juego-lichess.csv")