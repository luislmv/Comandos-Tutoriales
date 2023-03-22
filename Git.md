# Comandos de Git

## Información (versión y ayuda)

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
## Configuraciones generales de Git

```zsh
#Establece el nombre de mi usuario git.
git config --global user.name "luislmv" 

#Establece el correo electrónico de mi usuario git.
git config --global user.email "muniz.valledor.luis@ciencias.unam.mx"

#Establece el editor por defecto (NeoVim).
git config --global core.editor "nvim"

#Este alias compacta (-s de --short) la salida de "status", pero añade la información de la rama (-b de --branch).
git config --global alias.s "status -sb"

#Este alias compacta de una manera muy elegante la salida de "log".
git config --global alias.lg "log --oneline --decorate --all --graph"

#Similar al anterior, pero mucho mejor, ya que da mejor formato.
git config --global alias.lg "log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)' --all"

#Establece el nombre de la rama principal (Cambia de master a main).
git config --global init.defaultBranch main

#Configura a git (linux y mac, en windows cambiar "input" por "true") para que maneje correctamente los saltos de linea.
git config --global core.autocrlf input

#Muestra los parámetros que se han configurado.
git config --global --list 

#Editar el archivo de configuración.
git config --global -e
```
## Nuevo repositorio e información de su estado

Crear un repositorio en el directorio actual
```zsh
#Crea la carpeta ".git" donde se guardará toada la información del repositorio en el directorio actual.
git init
```
Conocer el estado actual del repesitorio
```zsh
git status
```
## Añadir archivos al Stage (escenario)

Añadir y eliminiar archivos del stage
```zsh
#Añade <nombre-archivo> al stage (sólo funciona si hay cambios en <nombre-archivo> o si, por alguna razón, aún no se le da seguimiento a nombre-archivo).
git add nombre-archivo

#Añade nombre-archivo-1 y nombre-archivo-2 al stage.
git add nombre-archivo-1 nombre-archivo-2

#Añade todos los archivos con extensión ".ext" del directorio raíz del proyecto (donde esta .git) al stage.
git add *.ext

#Añade todos los archivos con extensión ".ext" del subdirectorio "path-dir/" del proyecto al stage.
git add path-dir/*.ext

#Añade todos los archivos del subdirectorio "path-dir/" del proyecto al stage.
git add path-dir/

#Añade todos los archivos al stage (igual, sólo los que tienen cambios o a los que aún no se les da seguimiento).
git add .

#Elimina el archivo zshrc del nombre-archivo.
git reset nombre-archivo
```
Git no da seguimiento a directorios vacíos. Para que sí lo haga, hay que añadir en el directorio vacío un archivo oculto vacío con el nombre `.gitkeep`. Luego se le puede dar seguimiento a este archivo y por extensión al directorio "vacío".

## Crear commits

Tomar una fotografía del estado actual del proyecto (hacer un commit)
```zsh
#Toma una fotografía de los archivos en el escenario.
git commit -m "Comentario descriptivo en le commit"

#Añade todos los archivos al stage y les tota una fotografía (equivale a "add ." sequido del un "commit -m", sólo añade los archivos a los que se les ha dado seguimiento, pero que tienen cambios pendientes).
git commit -am "Comentario descriptivo en le commit"
```
## Moverse por la historia del repositorio
Reestablecer el repositorio al estado del último commit
```zsh
git checkout -- .
```
## Ramas del repositorio
Mostrar información de la ramas del repositorio
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
