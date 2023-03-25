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

Crear nuevas ramas
```zsh
#Crea una rama llamada "nombre-rama".
git branch nombre-rama

#Cambia a la rama "nombre-rama".
git checkout nombre-rama

#Crea una rama llamada "nombre-rama" y se cambia a la misma.
git checkout -b nombre-rama
```

Cambiar el nombre de las ramas
```zsh
#Cambia el nombre de la rama de nombre-viejo a nombre-nuevo.
git branch -m nombre-viejo nombre-nuevo
```

Unir ramas
```zsh
#Se mueve a "nombre-rama1" (que se supone está desfasada respecto a "nombre-rama2"). 
git checkout nombre-rama1

#Actualiza "nombre-rama1" con todos los commits de "nombre-rama2".
git merge nombre-rama2
```
Al realizar un `merge` pueden darse 3 escenarios distintos:
- La rama más atrasada ("nombre-rama1") no tiene commits, mientras "nombre-rama2" tiene uno o más commits que "nombre-rama1".
  En este caso, al hacer el `merge` se aplica la estrategia (automática) "Fast-Forward". La cual consite en añadir de todos los commits nuevos de "nombre-rama2" en "nombre-rama1".

- Ambas ramas "nombre-rama1" y "nombre-rama2" tienen commits que no están presentes en la otra, pero las modificaciones están en archivos diferentes o en parte diferentes de un mismo archivo, de manera que **Git** es capás de mezclar toda la información de manera automtica (no hay conflicto). En este caso, se usa una estrategia llamada "Recursive". Esta estrategia requiere un commit especial ("merge commit") en el cual se especifica (se abre un editor de código para que se escriba el mensaje del commit) el motivo por el cual es necesario hacer el `merge`.

-  Ambas ramas "nombre-rama1" y "nombre-rama2" tienen commits que no están presentes en la otra, pero las modificaciones están presentes en las mismas lines de los mismos archivos (si además hay cambios como en el caso anterior, estos se resuelven de manera automática). En este caso, **Git** no es capás de mezclar toda la información de manera automtica (hay conflicto). Por tanto, hay que editar manualmente los archivos donde hay conflicto para solucionarlo. Las lineas donde hay conflicto apareceran duplicadas y remarcadas (una por cada rama) para facilitar la edición. Es muy recomendable usar editores como  **VSCode** porque resaltan las diferencias con colores, además provee algunos botones con opciones predeterminadas para la resolución del conflicto. Finalmente, hay que hacer un commit con el resultado de la solución del conflicto.

Eliminar ramas
```zsh
#Elimina la rama "nombre-rama". Debemos de estar situados en una rama diferente. Da error si "nombre-rama" tiene commits que no se han integrado "merge" en alguna otra rama existente en el repo.
git branch -d nombre-rama

#Elimina (a la fuerza, es decir, no da error si hay commits que no estan presentes en las otras ramas) la rama "nombre-rama". Debemos de estar situados en una rama diferente.
git branch -D nombre-rama

#Igual que la anterior.
git branch -d nombre-rama -f
```
## Etiquetas (tags)

```zsh
#Crea una etiqueta (que apunta al último commit de la rama actual) llamada "nombre-tag". Puede ser para destacar una versión importante, candidata o final.
git tag nombre-tag

#Crea una etiqueta anotada para el último commit en la rama actual. Donde, "nombre-tag" (va entrecomillado a diferencia de la forma anterior) es el nombre de la etiqueta. Adicionalmete va acompañado de un mensaje más detallado (necesidad, importación, motivación, situación o estado del proyecto, etc.) para la etiqueta.
git tag -a "nombre-tag" -m "Mensaje explicativo de la etiqueta."

#Similar al caso previo, pero habre un editor para añadir el mensaje.
git tag -a "nombre-tag"

#Crea una etiqueta anotada en el commit cuyo hash es "n-hash" (por ejem: 5825c22). Esto se usa para añadir etiquetas en cualquir punto de la historia del repo (en cualquier commit de cualquier rama).
git tag -a "nombre-tag" -m "Mensaje explicativo de la etiqueta." n-hash

#Muestra todas las estiquetas en el repo.
git tag

#Elimina la etiqueta llamada "nombre-tag".
git tag -d nombre-tag
```
Se recomienda que `nombre-tag` tenga una estructura cemática del tipo `vN.M.K` por ejem: `v1.0.3`. Donde `N`, `M` y `K` son números enteros que representan distintos niveles de importancia de la versión. Más detalladamente, el número `N` representa una versión mayuor, en la cual hay grandes cambios y puede ser incompatible con versiones previas. El número `K` representa pequeñas correcciones de erros detectados, etc. (cambios menores). El número `M` puede tener cambios más importantes, pero no tan grandes como para generar incompatibilidad o romper partes de la versión previa.
