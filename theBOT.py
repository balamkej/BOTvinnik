#! /usr/bin/env python

import tweepy
import BOTvinnik as b
import board_renderer as br
import time

auth = tweepy.OAuthHandler()
auth.set_access_token()
api = tweepy.API(auth)

game = b.randomGame()
moves = b.getMoves(game)
board = b.randomBoard(moves,game)

renderer = br.DrawChessPosition()
fen = board.fen().split(" ")[0]
answerBoard = renderer.draw(fen)
answerBoard.save("answerBoard.png")

move = board.pop()
answerText = "He played %s." % board.san(move) 

questionText = b.question(game)

renderer = br.DrawChessPosition()
fen = board.fen().split(" ")[0]
questionBoard = renderer.draw(fen)
questionBoard.save("questionBoard.png")

api.update_with_media("questionBoard.png", status = questionText)

time.sleep(60)

public_tweets = api.user_timeline()
last_status_id = public_tweets[0].id
api.update_with_media("answerBoard.png", status = "@BOTvinnikBOT " + answerText, in_reply_to_status_id = last_status_id)