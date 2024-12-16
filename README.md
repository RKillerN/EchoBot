# EchoBot
Bot de Telegram básico que repite ("echo") los mensajes recibidos, basado en windows.

## 1. Creación de las ramas necesarias para el proyecto
En este repositorio se encuentran tres ramas:
  - main
  - features/hello
  - develop
Estas ramas contienen todo lo necesario para el funcionamiento del bot de echo de telegram.

## 2. Crear y activar el entorno virtual
En este apartado crearemos el entorno virtual, para crearlo aplicamos el siguiente comando:
*python -m venv venv*
Una vez creado se activa de la siguiente manera:
*venv/Scripts/actibate.bat*
Dentro de venv instalamos las dependencias y guardar todas las dependencias en requirements.txt:
Instalar el bot de Telegram-->*pip install python-telegram-bot*
Guardar las dependencias utilizadas-->*pip freeze > requirements.txt*
De esta manera tendremos lo necesario para continuar.

## 3. Configurar archivos
El primer archivo a crear es el archivo config.py donde guardaremos el token de Telegram, este token se consiguen desde el BotFather, creando un bot para el proyecto, para pedirle el token del bot le pedimos a BotFather con /Token.

Después creamos el archivo .gitignore para añadir lo siguiente a este archivo:
*venv/*
*config.py*
De esta manera ignoramos la ruta venv/ y config.py.

Por último creamos el archivo bot.py, el código del archivo se encuentra disponible en el proyacto, en resumen crea la aplicación para que el bot repita los mensages enviados.

## 4. Probar el programa EchoBot
Para probarlo ejecutamos el siguiente comando:
*python bot.py*

Para verificar su funcionamiento es abriendo Telegram y accedemos a nuestro bot creado al inicio del proyecto. Con el comando */start* iniciaremos  la conversación señalando el siguiente mensage "Soy un bot de eco".

## 5. Gestión final de las ramas de GitHub del proyecto
Desde la rama develop, desde cmandos sería *git checkout develop*, luego fusionamos la rama features/hello con develop, desde comandos sería *git merge feature/hello* y realizamos un push al origen cambiando a la rama main la fusionamos con develop *git merge develop* y realizando un push *git push origin main*.

De esta manera el proyecto EchoBot queda funcionando.
