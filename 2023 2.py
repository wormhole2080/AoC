# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 19:37:37 2023

@author: gspij
"""
import  functools

RGB = tuple[int, int, int]
Game = tuple[int, list[RGB]]

def sol(part):
    possible_games=[]
    
    with open("2023 2.txt") as input_file:
        lines = input_file.read().strip().split('\n')
        games=[]
        for line in lines:
            games.append(parse_game(line))
        
        for game in Games:
            if possible_game(game[1]):
                possible_games.append(game[0])
                
    return sum(summed)

def possible_game(rgb : RGB) ->bool:
    return all(r <=12 and g <=13 and b <=14 for r, g, b in rgb)
        
def parse_game(line: str) -> Game:
    id, subsets = line.split(": ")
    return int(id.split(" ")[-1]), [parse_rgb(x) for x in subsets.split("; ")]

def parse_rgb(rgb: str) -> RGB:
    r, g, b = 0, 0, 0
    for value in rgb.split(", "):
        n, color = value.split(" ")
        match color:
            case "red":
                r = int(n)
            case "green":
                g = int(n)
            case "blue":
                b = int(n)

    return r, g, b
if __name__ == "__main__":
    print(sol(1))
    print(sol(2))
    