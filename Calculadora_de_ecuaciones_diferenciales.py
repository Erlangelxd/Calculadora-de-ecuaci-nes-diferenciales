import sympy as sp
#De orden 2======================================================
def Orden_2(): # Definimos las variables simbólicas
  x, y = sp.symbols('x y')
  y = sp.Function('y')(x)
  print("Ingrese los coeficientes de la ecuación diferencial:")
  a = sp.sympify(input("a: "))
  b = sp.sympify(input("b: "))
  c = sp.sympify(input("c: "))
  eq = sp.Eq(a*sp.diff(y, x, 2) + b*sp.diff(y, x) + c*y, 0) #La ecuación debe estar en la forma a*y'' + b*y' + c*y = 0
  sol_y = sp.dsolve(eq, y) #Resuelve la ecuación diferencial
  sol_str = str(sol_y)
  sol_str = sol_str.replace("**", "^").replace("*", "")
  print("La solución general de la ecuación diferencial es:")
  print(sol_str)
#De orden 3======================================================
def Orden_3():
  x, y = sp.symbols('x y')
  y = sp.Function('y')(x)
  print("Ingrese los coeficientes de la ecuación diferencial:")
  a = sp.sympify(input("a: "))
  b = sp.sympify(input("b: "))
  c = sp.sympify(input("c: "))
  d = sp.sympify(input("d: "))
  eq = sp.Eq(a*sp.diff(y, x, 3) + b*sp.diff(y, x, 2) + c*sp.diff(y, x) + d*y, 0) #Forma
  sol_y = sp.dsolve(eq, y) #Resuelve la ecuación diferencial
  sol_str = str(sol_y)
  sol_str = sol_str.replace("**", "^").replace("*", "")
  print("La solución general de la ecuación diferencial es:")
  print(sol_str)
#De orden 4======================================================
def Orden_4():
  x, y = sp.symbols('x y')
  y = sp.Function('y')(x)
  print("Ingrese los coeficientes de la ecuación diferencial:")
  a = sp.sympify(input("a: "))
  b = sp.sympify(input("b: "))
  c = sp.sympify(input("c: "))
  d = sp.sympify(input("d: "))
  e = sp.sympify(input("e: "))
  eq = sp.Eq(a*sp.diff(y, x, 4) + b*sp.diff(y, x, 3) + c*sp.diff(y, x, 2) + d*sp.diff(y, x) + e*y, 0) #Forma
  sol_y = sp.dsolve(eq, y) #Resuelve la ecuación diferencial
  sol_str = str(sol_y)
  sol_str = sol_str.replace("**", "^").replace("*", "")
  print("La solución general de la ecuación diferencial es:")
  print(sol_str)
#Menu==================================
def Menu():
  print("\n--- Menú ---")
  print("1. Ecuación de 2do orden")
  print("2. Ecuación de 3er orden")
  print("3. Ecuación de 4to orden")
  print("4. Salir")
#======================================
if __name__ == "__main__":
  while True:
    Menu()
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
      Orden_2()
    elif opcion == "2":
      Orden_3()
    elif opcion == "3":
      Orden_4()
    elif opcion == "4":
      break
    else:
      print("Opción inválida.")