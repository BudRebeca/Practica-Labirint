import random

def generate_maze(rows, cols, start, end, complexity=0.1):
    maze = [[' ' for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if random.uniform(0, 1) < complexity or (i == start[0] and j == start[1]) or (i == end[0] and j == end[1]):
                maze[i][j] = '#'

    maze[start[0]][start[1]] = 'S'
    maze[end[0]][end[1]] = 'E'

    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(row))

def is_valid(x, y, maze):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#'

def find_exit(maze, start, end):
    stack = [(start[0], start[1])]
    visited = set()

    while stack:
        x, y = stack.pop()

        if (x, y) == end:
            return True

        if (x, y) not in visited:
            visited.add((x, y))

            #Se verifica si se adauga vecinii nevizitati in stiva de exploarere
            neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            stack.extend((nx, ny) for nx, ny in neighbors if is_valid(nx, ny, maze))

    return False

def main():
    rows, cols = 5, 5
    start = (0, 0)
    end = (rows-1, cols-1)

    maze = generate_maze(rows, cols, start, end)
    print("Labirintul generat:")
    print_maze(maze)

    if find_exit(maze, start, end):
        print("\nExista o cale de iesire!")
    else:
        print("\nNu exista nicio cale catre iesire!")

if __name__== "__main__":
    main()


#_________________________________________________________________________________________________________________________
#generate_maze(rows, cols, start, end, complexity=0.1): Această funcție generează un labirint cu dimensiunile specificate
#(rows x cols). Parametrii start și end reprezintă pozițiile de start și de sfârșit în labirint. Parametrul opțional
#complexity controlează cât de dens va fi labirintul (procentajul de ziduri).

#print_maze(maze): Această funcție afișează labirintul în consolă. ' ' reprezintă spațiu liber,
# '#' reprezintă un perete, 'S' reprezintă start, iar 'E' reprezintă ieșire.

#is_valid(x, y, maze): Această funcție verifică dacă o poziție specificată de
# coordonate (x, y) este validă în labirint, adică nu depășește limitele și nu este un perete.

#find_exit(maze, start, end): Această funcție folosește căutarea în adâncime
# pentru a verifica dacă există o cale între poziția de start și cea de sfârșit în labirint.

#main(): Această funcție inițializează dimensiunile labirintului, pozițiile de start și sfârșit,
# apoi generează și afișează labirintul. Apoi, verifică dacă există o cale între start și sfârșit
# folosind find_exit și afișează un mesaj corespunzător.

#_________________________________________________________________________________________________________________________




#_________________________________________________________________________________________________________________________

#Generarea labirintului (generate_maze):
#Funcția primește dimensiunile labirintului (rows, cols), poziția de start (start), poziția de sfârșit (end) și un parametru opțional complexity care controlează gradul de dificultate al labirintului.
#Labirintul este reprezentat printr-o listă bidimensională (maze) inițializată cu spații goale (' ').
#Caracterele '#' sunt plasate aleatoriu în labirint, simulând zidurile. Se asigură că pozițiile de start și sfârșit sunt libere.
#Funcția returnează labirintul generat.


#Afișarea labirintului (print_maze):
#Această funcție primește labirintul și îl afișează pe ecran într-un mod ușor de citit.
#Caracterele specifice sunt folosite pentru a reprezenta spațiile libere, zidurile, punctul de start și punctul de sfârșit.


#Validarea unei poziții (is_valid):
#Verifică dacă o anumită poziție (x, y) este validă în cadrul labirintului.
#Se asigură că poziția nu depășește limitele labirintului și nu corespunde unui perete.


#Căutarea căii (find_exit):
#Folosește căutarea în adâncime pentru a verifica dacă există o cale între poziția de start și cea de sfârșit.
#Se utilizează o stivă pentru a explora în mod recursiv vecinii valizi ai unei poziții.
#Se marchează pozițiile vizitate pentru a evita bucle infinite.
#Dacă poziția de sfârșit este atinsă, funcția returnează True, altfel returnează False.


#Funcția principală (main):
#Inițializează dimensiunile labirintului, pozițiile de start și sfârșit.
#Generează și afișează labirintul utilizând funcțiile anterioare.
#Apoi, verifică dacă există o cale între poziția de start și cea de sfârșit, și afișează un mesaj corespunzător.


#Alte informații:
#Parametrul complexity în generate_maze poate fi ajustat pentru a obține labirinte mai complexe sau mai simple.
#Se poate modifica dimensiunile labirintului sau alte aspecte ale aplicației pentru a se potrivi nevoilor dvs.

#_________________________________________________________________________________________________________________________