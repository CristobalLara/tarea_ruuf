# Tarea Dev Junior - Ruuf

## 🎯 Objetivo

El objetivo de este ejercicio es poder entender tus habilidades como programador/a, la forma en que planteas un problema, cómo los resuelves y finalmente cómo comunicas tu forma de razonar y resultados.

## 🛠️ Problema

El problema a resolver consiste en encontrar la máxima cantidad de rectángulos de dimensiones "a" y "b" (paneles solares) que caben dentro de un rectángulo de dimensiones "x" e "y" (techo).

## 🚀 Cómo Empezar

### Solución en Python
```bash
cd python
python main.py
```

## ✅ Casos de Prueba

Tu solución debe pasar los siguientes casos de prueba:
- Paneles 1x2 y techo 2x4 ⇒ Caben 4
- Paneles 1x2 y techo 3x5 ⇒ Caben 7
- Paneles 2x2 y techo 1x10 ⇒ Caben 0

---

## 📝 Tu Solución

Explica acá

Uno podria pensar que solo con calcular el area a abarcar, dividida por el area de los paneles uno obtendria el numero de paneles que caben en un techo. Pero como no sabemos si caben mas paneles en posicion horizontal o vertical, hay que evaluar los diferentes casos:

1. Caben mas paneles horizontales que verticales, o viceversa.
2. Caben mas paneles con una combinacion de paneles horizontales y verticales.
3. Cuando el espacio es superado por un panel extra, es decir no cabe un panle por falta de espacio.

Para resolver estas dudas y ahorrar espacio de codigo cree una nueva funcion llamada *max_panles*, la cual analiza el espacio sobrante utilizando una orientacion vertical u horizontal dominante, es decir cuantos paneles verticales caben apilados en una direccion y el espacio sobrante para seguir apilando, y determinar el maximo de paneles usados.
# Linea 6
```bash
for i in range(roof_h // panel_h + 1):
```

Intentamos colocar paneles hasta el máximo numero de filas verticales que caben (con panel_h de alto), con i representando cuantas filas de paneles verticales intentamos poner.
# Linea 9
```bash
vertical_panels = i * (roof_w // panel_w):
```

En cada fila vertical caben (roof_w // panel_w) paneles de ancho, multiplicado por i filas, da el total de paneles verticales que hemos puesto.
# Linea 10
```bash
horizontal_panels = (remaining_height // panel_w) * (roof_w // panel_h):
```

En el espacio restante, colocamos paneles rotados (de costado).Su ancho pasa a ser panel_h y su alto panel_w, y asi calculamos cuantos caben horizontalmente en ese espacio restante.

Una vez se calculan estas estimaciones, *calculate_panles* entrega el maximo entre dos funciones de max_panels con los paneles en orientaciones contrariasn y entrega la que cuente con un mayor numero de paneles utilizados para completar el espacio.

---

## 💰 Bonus (Opcional)

No complete el bonus, ya que considere que me llevaria mas tiempo y esta vez quisera priorizar la entrega de la solucion principal.

## 🤔 Supuestos y Decisiones

Tuve que agregar una funcion llamada max_panels para ahorrar espacio de codigo.

