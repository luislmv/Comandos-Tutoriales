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

#Elimina el archivo nombre-archivo del stage.
git reset nombre-archivo
```
Git no da seguimiento a directorios vacíos. Para que sí lo haga, hay que añadir en el directorio vacío un archivo oculto vacío con el nombre `.gitkeep`. Luego se le puede dar seguimiento a este archivo y por extensión al directorio "vacío".

Para evitar que **Git** le de seguimiento a ciertos archivos o directorios (por ejem.: archivos que se generan de manera automática durante la compilación etc.) se deben especificar dentro de un archivo `.gitignore` en la raiz del repo (en el mismo directorio qe `.git`). También se pueden especificar todos los archivos con cierta extensión (`*.ext`). Ejemplo de archivo `.gitignore`:

```zsh
nombre-archivo-nosegido
nombre-directorio-no-seguido/
*.ext
```

## Crear commits

Tomar una fotografía del estado actual del proyecto (hacer un commit)
```zsh
#Toma una fotografía de los archivos en el escenario.
git commit -m "Comentario descriptivo en le commit"

#Añade todos los archivos al stage y les tota una fotografía (equivale a "add ." sequido del un "commit -m", sólo añade los archivos a los que se les ha dado seguimiento, pero que tienen cambios pendientes).
git commit -am "Comentario descriptivo en le commit"

#Cambia el comentario del último commit por "Nuevo comentario descriptivo".
git commit --amend -m "Nuevo comentario descriptivo"

#Abre el editor por defecto (vim, nvim, etc.) para editar manualmente la info. (comentario, cambios en el commit, etc.) del último commit. 
git commit --amend
```

## Encontrar cambios en los archivos

```zsh
#Muestra los cambios en el estado actual de los archivos modificados (que no están agregados al stage) respecto al estado de los mismos en el último commit (si algún archivo no tiene commit, los cambios de ese archivo no se mostrarán).
git diff

#Muestra los cambios en el estado actual de los archivos en el stage respecto al estado del último commit (tambien muestra los cambiso de los archivos que no tiene commit aún).
git diff --staged
```
Lo anterior es muy util, pero es mucho más cómodo usar la interfaz visual de los editores (por ejemm. **VSCode**).

## Renombrar (mover) y eliminar archivos

```zsh
#Cambia el nombre (se mueve en el mismo directorio pero con otro nombre) de "nombre-viejo" a "nombre-nuevo" en el directorio actual.
git mv nombre-viejo nombre-nuevo 

#Elimina a nombre-archivo del directorio actual
git rm nombre-archivo
```
Los archivos remobrados o eliminados pasan al `stage` (con un identificador `R` o `D`), para que al hacer commit quede asentado que se han renombrado o eliminado.

Si el renombrado o la eliminación se hacen de manera manual (desde el explorador de archivos o demanera gráfica en el editor), los archivos renombrados aparecerán duplicados en el `status` (eliminado con el nobre viejo -con letra `D`- y no añadido al repo con el nombre nuevo -letra `U`-) y los eliminado con letra "D". En ambos caso los cambios no estarán en el `stage` (a diferencia del caso anterior). Al agregarlos al `stage` (`git add .`), **Git** revisa los archivos que hemos renombrado manualmte y resuelve el problema (le coloca la letra `R`). Al hacer el commit, quedan registrados los cambios de nombres y las eliminaciones.

## Moverse por la historia del repositorio

Reestablecer el repositorio al estado del último commit
```zsh
#Deshace todos los cambios en el proyecto posteriores al último commit. No afecta a los archivos en el stage.
git checkout -- .

#Hace lo mismo, pero deja un registro de esta acción. El cual se puede ver con "git reflog". Además sí afecta a los archivos en el stage.
git reset --hard

#Mueve el estado del repo al estado del último commit. Modifica los archivos para dejarlos en ese estado, pero no destruye los commits, por tanto se puede regresar al estado del último commit y recuperar todos los cambios (no funciona en zsh).
git checkout HEAD^

#Igual que el anterior pero funcina tanto en bash como en zsh.
git checkout HEAD^

#Mueve el estado del repo al estado anterior a los últimos "i-1" commits (no zsh). Da error si hay cambios que no han sido respaldados por un commit.
git checkout HEAD^i

#Igual que el anterior (bash, zsh).
git checkout HEAD^i

#Elimina el último commit sin deshacer los cambios en los archivos (no zsh).
git reset --soft HEAD^

#Igual que el anterior (bash, zsh).
git reset --soft HEAD~

#Elimina los últimos 'i' commits realizado (no zsh). No afecta a los archivos ni al stage.
git reset --soft HEAD^i

#Igual que el anterior (bash, zsh).
git reset --soft HEAD~i

#Elimina los últimos 'i' commits realizado, saca del stage (y deja de dar seguimientos) a todos los archivos añadidos al stage en esos commits. No afecta a los archivos
git reset --mixed HEAD~i 
git reset HEAD~i #--mixed es la opción por defecto.

#Elimina los últimos 'i' commits realizado. Elimina todo lo creado en esos commits (regresa al repo a ese estado). 
git reset --hard HEAD~i
```
Se puede especificar el punto exacto dcel historial al cual nos queremos mover. Sólo hay que sustituir `HEAD~i`por el hash corto largo correspondiente en el historial (por ejem. `b8c5057`). Esto funciona con `reset` y con `checkout`.

Todos los cambios (destructivos o no) se registran en un historial, por tanto, siempre se pueden recuperar (incluso si se ha usado `--hard`).

```zsh
#Muestra todos los cambios (con sus respectivos hash) en el respo. comits, resets, checkout, etc. 
git reflog
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
