# Animaciones con Manim

## Pagina web

En [este enlace](https://docs.manim.community/en/stable/) se puede acceder a toda la documentación incluyendo las instrucciones de instalación.

## Crear animación

```shell
# Crear la animación con el código de "nombre-scrip.py"
manim nombre-scrip.py

# Crear una previsualización de la animación con el código de "nombre-scrip.py" y la muestra.
manim -pqm nombre-scrip.py
```

## Pilares de manim

- **Clase Mobject**

    Los objetos en el camva que se van a animar.

- **Clase Animation**e

    Las transfomaciones para animar los mobjetos.

- **Clase Scene**

    El canva donde se muestran los mobjetos animados.

## Dimensiones de la pantalla

El origen `[0, 0, 0]` se encuentra en el centro de la pantalla (tradicionalmente se ubica en la esquina superior derecha, ya que la pantalla se considera como una matriz cuya dimensión determina la resolución de la misma).

### Constantes de posicionamiento

Las siguientes constantes definen la posición (por medio de un vector de pasos, no de pixeles) de los objetos:

- `ORIGIN` corresponde a la posición del al vector `[0, 0, 0]`.
- `UP` corresponde a la posición del al vector `[0, 1, 0]`.
- `DOWN` corresponde a la posición del al vector `[0, -1, 0]`.
- `RIGHT` corresponde a la posición del al vector `[1, 0, 0]`.
- `LEFT` corresponde a la posición del al vector `[-1, 0, 0]`.

La cantidad de píxeles que representan estos pasos dependerá de la transformación en la que se utilicen dichas constantes.

Para conocer más constantes, revisar [este](https://docs.manim.community/en/stable/reference/manim.constants.html#module-manim.constants) enlace.

## Transformaciones

- `scale()` 
- `shift(pos)`
- `next_to(mobject, pos)`
- `to_edge(pos)`
- `to_corner(pos)`
- `move_to(pos)`
- `align_to()`

## Otros métodos de Mobject

- `set_fill(color)`

## Animaciones

Existen dos manera de realizar animaciones en __Manim__.

- Método animation

    Se pueden generar mediante el método `animation` de cualquier objeto `mobject`. Este anima los cambios en los atributos de `mobject` que se producen mediante otros métodos de `mobject`En resumen, es un método que anima los cambios de producen otros métodos en los atributos de un objeto mobject.

- Mediante la clase Animation

## Agregar objetos a la escena

```python
#Añade un objeto a la escena sin animaciones.
self.add(objeto)

#Añade un objeto a la escena con animaciones.
self.play(objeto-animado)
```

## Transformaciones

```python
#Transforma "ob-original" en "ob-final" sin desaparecer "ob-original" De hecho ambos objetos están visibles pero superpuestos.
Transform(ob-original, ob-final)

#Transforma "ob-original" en "ob-final" pero elimina "ob-original". El objeto original se elimina de la memoria y la pantalla.
ReplacementTransform(ob-original, ob-final)
```