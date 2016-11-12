#! /usr/bin/env python

import chess, chess.pgn, random

def randomGame():
	game_num = random.randint(0,800)
	pgn = open('botvinnik.pgn')
	for i in range(game_num):
		game = chess.pgn.read_game(pgn)
	pgn.close()
	return game

def getMoves(game):
	moves = list(game.main_line())
	return moves

def randomBoard(moves,game):
	board = chess.Board()
	if game.headers['Black'] == 'Botvinnik, Mikhail':
		move_num = random.randrange(10,len(moves)-2,2)
	else:
		move_num = random.randrange(10,len(moves)-2,2)+1
	for i in range(move_num):
		board.push(moves[i])
	return board

def question(game):
	if game.headers['Black'] == 'Botvinnik, Mikhail':
		text = "Here Botvinnik had black against %s in the %s. What did Mikhail play?" % (game.headers['White'].split(",")[0],game.headers['Event'])
	else:
		text = "Here Botvinnik had white against %s in the %s. What did Mikhail play?" % (game.headers['Black'].split(",")[0],game.headers['Event'])
	return text