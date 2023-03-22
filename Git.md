# Comandos básicos de Git

Conocer la versión actual de git
```zsh
git --versión
```
Desplegar la ayuda de git
```zsh
#Despliega la ayuda en general.
git --help

#O tamibén.
git help

#Se puedce desplegar la ayuda de algún comando dentro de git (por ejemp. commit).
git help commit
```
Configuraciones generales de Git
```zsh
#Establece el nombre de mi usuario git.
git config --global user.name "luislmv" 

#Establece el correo electrónico de mi usuario git.
git config --global user.email "muniz.valledor.luis@ciencias.unam.mx"

#Establece el editor por defecto (NeoVim).
git config --global core.editor "nvim"

git config --global alias.s "status -sb"

git config --global alias.lg "log --oneline --decorate --all --graph"

#Establece el nombre de la rama principal (Cambia de master a main).
git config --global init.defaultBranch main

#Configura a git (linux y mac, en windows cambiar "input" por "true") para que maneje correctamente los saltos de linea.
git config --global core.autocrlf input

#Muestra los parámetros que se han configurado.
git config --global --list 

#Editar el archivo de configuración.
git config --global -e
```
Crear un repositorio en el directorio actual
```zsh
#Crea la carpeta ".git" donde se guardará toada la información del repositorio en el directorio actual.
git init
```
Conocer el estado actual del repesitorio
```zsh
git status
```
Añadir y eliminiar archivos del stage (escenario)
```zsh
#Añade zshrc al stage (sólo funciona si hay cambios en zshrc o si, por alguna razón, aún no se le da seguimiento a zshrc).
git add zshrc

#Añade todos los archivos al stage (igual, sólo los que tienen cambios o a los que aún no se les da seguimiento).
git add .

#Elimina el archivo zshrc del stage.
git reset zshrc
```
Tomar una fotografía del estado actual del proyecto (hacer un commit)
```zsh
#Toma una fotografía de los archivos en el escenario.
git commit -m "Comentario del en le commit"

#Añade todos los archivos al stage y les tota una fotografía (equivale a "add ." sequido del un "commit -m").
git commit -am "Comentario del en le commit"
```
Reestablecer el repositorio al estado del último commit
```zsh
git checkout -- .
```
Mostrar información de lar ramas del repositorio
```zsh
#Muesta las ramas en el proyecto, se resalta la rama en la que estamos trabajando actualmente.
git branch

#También muestra esta información.
git status
```
Cambiar el nombre de las ramas
```zsh
#Cambia el nombre de la rama de nombre-viejo a nombre-nuevo.
git branch -m nombre-viejo nombre-nuevo
```
