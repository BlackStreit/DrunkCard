# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 21:04:23 2024

@author: Admin
"""

from Deck import Deck
from Player import Player
class Game:
	def __init__(self):
		name1 = input("ВВедите имя первого игрока: ")
		name2 = input("ВВедите имя второго игрока: ")
		self.deck = Deck()
		self.p1 = Player(name1)
		self.p2 = Player(name2)
	
	def wins(self, winner):
		w = f"{winner} забирает карты"
		print(w)
		
	def draw(self, p1n, p1c, p2n, p2c):
		d = f'{p1n} кладет {p1c}, a {p2n} кладет {p2c}'
		print(d)
		
	def winner(self, p1, p2):
		if p1.wins > p2.wins:
			return f'{p1.name} одержал победу'
		if p1.wins < p2.wins:
			return f'{p2.name} одержал победу'
		return "Ничья!"
	
	def play_game(self):
		cards = self.deck.cards
		print("Поехали!")
		while len(cards)>0:
			m = "Нажмите X для выхода. Нажмите любую другую клавишу для начала игры: "
			responce = input(m)
			if responce == 'X':
				break
			
			p1c = self.deck.rm_card()
			p2c = self.deck.rm_card()
			p1n = self.p1.name
			p2n = self.p2.name
			
			self.draw(p1n, p1c, p2n, p2c)
			if (p1c > p2c):
				self.p1.wins+=1
				self.wins(self.p1.name)
			else:
				self.p2.wins+=1
				self.wins(self.p2.name)
			
			win = self.winner(self.p1, self.p2)
			print(f"Игра окончена! {win}")
			