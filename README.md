# Carrusel Instagram — Seguridad PBA

Seis placas verticales (1080 × 1350 px), con fondo `#b7b6b7`, pensadas como una secuencia narrativa para Afiches. El repositorio contiene únicamente los SVG editables y el código fuente: los SVG se regeneran con `python3 generate_carousel.py` y, si se necesitan, los PNG se producen localmente con `python3 render_png.py`.

## Walkthrough: qué hace cada momento

1. **Frenar el scroll.** Abrimos con una pregunta que convierte “la inseguridad” en una experiencia concreta y enseguida revelamos el dato más fuerte: **37% de los hogares sufrió un hecho en el último año**.
2. **Dimensionar el clima.** Pasamos del hecho a la sensación: **51% se siente poco o nada seguro**, y anclamos la conversación en la preocupación dominante: robos y asaltos (50%).
3. **Ubicar la brecha.** Mostramos que el fenómeno no es homogéneo: el Conurbano registra **41% de victimización y 63% de inseguridad**, frente a 31% y 41% en el resto de PBA.
4. **Explicar el impacto.** Cruzamos experiencia y percepción: **72% de las víctimas** se siente poco o nada segura, una brecha de 33 puntos frente a quienes no fueron víctimas.
5. **Presentar el diferencial de Afiches.** La frase “Pero lo más importante: lo medimos en las propias palabras de las personas” introduce el entrevistador IA. Una voz real hace visible cómo una vivencia cotidiana cambia hábitos, mientras el cierre explica la combinación de profundidad cualitativa y escala cuantitativa.
6. **Convertir interés en conversación.** Cerramos con una única acción, directa y fácil de medir: **“Comentá la publicación”** para recibir el informe completo.

## Archivos

- `carousel/01.svg`: portada / hook.
- `carousel/02.svg`: sensación y principal preocupación.
- `carousel/03.svg`: brecha territorial.
- `carousel/04.svg`: victimización y percepción.
- `carousel/05.svg`: testimonios e entrevistador IA.
- `carousel/06.svg`: llamada a la acción.
- `generate_carousel.py`: código fuente que genera las seis placas SVG.
- `render_png.py`: utilidad opcional para exportar PNG localmente; los binarios generados no se versionan.

## Cómo generar PNG localmente

Ejecutá `python3 render_png.py` desde la raíz del repositorio. Se crearán `carousel/01.png`–`carousel/06.png` en 1080 × 1350 px. Estos archivos están ignorados por Git para que el pull request contenga solo SVG y código fuente.

Los archivos `.svg` son las fuentes editables. Para publicar en Instagram, generá los `.png` localmente y subilos desde tu computadora.

> Los porcentajes y el testimonio reproducen las referencias provistas. Antes de publicar, conviene sumar en el copy de Instagram la ficha técnica, fecha de campo y base de la encuesta.
