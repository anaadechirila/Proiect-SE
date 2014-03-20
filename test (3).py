NONE, WALL, BEGN, FNSH, SEEN, GOOD = tuple(' *AB.+')

SAMPLE = """
***************
A       *     *
* ***** ***** *
* ****    *   *
* *   *** * * *
* * * *   * * * 
*   * * * * * *
***** * * * * *
*   *   *     B
***************
"""


""" on verifie si les elements de la matrice sont deja ou pas en refaisant le chemin en retournant si elle trouve de murs"""
def solution(maze, posx, posy, sizex, sizey):
    found = 0
    if 0 <= posx < sizex and 0 <= posy < sizey:
        if maze[posy][posx] in (NONE, BEGN):
            if maze[posy][posx] == NONE:
                maze[posy][posx] = SEEN
            if (solution(maze, posx+1, posy, sizex, sizey) or
                solution(maze, posx-1, posy, sizex, sizey) or
                solution(maze, posx, posy+1, sizex, sizey) or
                solution(maze, posx, posy-1, sizex, sizey)):
                if maze[posy][posx] == SEEN:
                    maze[posy][posx] = GOOD
                found = 1
        elif maze[posy][posx] == FNSH:
            found = 1
    return found

""" maze- prend une liste du caracere pour labyrinthe
    posx- la position de x
    posy- la position de y
    sizex, sizey- la dimension de la matrice """


def main():
    maze = [list(x) for x in SAMPLE.splitlines() if x]
    solution(maze, 0, 1, len(maze[0]), len(maze))
    for line in maze:
        print "".join(line)

if __name__ == "__main__":
    main()

"""l'initialisation du contructeur main pour resoudre le maze""" 
