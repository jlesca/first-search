colors = ['red', 'green', 'blue', 'yellow', 'black', 'white', 'brown'] # Creo la variable y asigno sus elementos
print(colors) # Muestro la variable de ejemplo
new_colors = [] # Creo una variable vacía donde se irá creando una lista con los resultados de la búsqueda.

letter = input('INPUT A LETTER TO SEARCH: ') # Creo una variable que tomará el valor que el usuario ingrese como texto.

for item in colors: # Creo la variable 'item' para cada elemento de la variable 'colors'.
  if letter in item: # Si el valor de 'letter' está incluido en la variable 'item', haga lo siguiente.
    new_colors.append(item) # Agregue a la variable 'new_colors' los valores tomados por la var 'item'
    
print('SHOW ME COLORS') # Muestro el título.
print(new_colors) # Muestro los resultados de la búsqueda.
input() # Salgo del programa.
