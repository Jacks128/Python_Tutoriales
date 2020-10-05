import random
import curses #libreria para hacer interfaces graficas con contro de teclado

s = curses.initscr() #inicializamos la pantalla de la interfaz
curses.curs_set(0) #esto es para que no se muestre el cursos
sh, sw = s.getmaxyx() #para obtener la altura y e ltamaña
w = curses.newwin(sh,sw, 0,0) #creamos una ventana nueva con la altura y ancho encontrados y el 0 0 es para que empiece en el top screen
w.keypad(1) #habilatamos el teclado
w.timeout(100) #refrescamos la pantalla cada 100mil milisegundos

snk_x = sw/4 #posicione en x de la serpiente
snk_y = sh/2 #posicion en y de la serpiente
snake = [ [snk_y, snk_x], [snk_y, snk_x-1], [snk_y, snk_x-2]] #dando le forma a la serpiente
food = [sh/2, sw/2] #dando posicion a la comida
w.addch(int(food[0]), int(food[1]), curses.ACS_PI) # agregando la comida a la pantalla

key = curses.KEY_RIGHT #obtener la tecla derecha

while True: #ciclo para obtener las teclas
    next_key = w.getch() #obtener cual es la siguiente tecla
    key = key if next_key == -1 else next_key #para tomar la siguiente tecla o tomar la que ya se tenia

    if snake[0][0] in [0, sh] or snake[0][1] in [0,sw] or snake[0] in snake[1:]: #perdemos el juego se la serpiente pasa los bordes o se come
        curses.endwin() #FINALIZAMOS LA INTERFZ
        quit()#CERRAMOS LA INTERFAZ

    new_head = [int(snake[0][0]), int(snake[0][1])] #PONER LA NUEVA CABEZA DE LA SERPIETNE

    if key==curses.KEY_DOWN: #SI LA TECLA ES LA DE ABAJO
        new_head[0] +=1
    elif key==curses.KEY_UP: #SI LA TECLA ES LA DE ARRIBA
        new_head[0] -=1
    elif key==curses.KEY_LEFT: #SI LA TECLA ES LA DE IZQ
        new_head[1] -=1
    elif key==curses.KEY_RIGHT: #SI LA TECLA ES LA DE DER
        new_head[1] +=1

    snake.insert(0, new_head)

    if snake[0] == food: #si la serpiente se come la comida
        food = None #poenmos la comida como vacia
        while food is None:
            nf = [ #creamos una nueva comida
                random.randint(1, sh-1), #con posiciones x y Y random
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None #agregamos la nueva comida a ffod
    else:
        tail = snake.pop() #obtenemos la cola de la serpiente 
        w.addch(int(tail[0]), int(tail[1]), ' ') #y la agregamos a la interfaz

    w.addch (int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)

