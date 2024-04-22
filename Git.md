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

#Este alias sirve para crear commits de manera más sencilla.
git config --global alias.com "commit -m"

#Este alias compacta de una manera muy elegante la salida de "log".
git config --global alias.lg "log --oneline --decorate --all --graph"

#Similar al anterior, pero mucho mejor, ya que da mejor formato.
git config --global alias.lg "log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)' --all"

#Establece el nombre de la rama principal (Cambia de master a main).
git config --global init.defaultBranch main

#Configura a git (linux y mac, en windows cambiar "input" por "true") para que maneje correctamente los saltos de linea.
git config --global core.autocrlf input

#Establece los colores para la salida de git (por defecto es "auto" que agrega colores a la salida estándar pero no lo hace si la salida se redirige a otros archivos o a comandos mediante tuberías). La opción "false" desactiva todo y "always" añade colores en todos los caso (salida estándar, archivos, tuberías, etc).
git config --global color.ui true

#Establece que sólo se use un fast-forward (ff) al actualizar el repo local desde el remoto (pull).
git config --global pull.ff only

#Establece que se pueda hacer un rabase interactivo (permite un merge si no se puede un fast-forward) al actualizar el repo local desde el remoto (pull) en caso de que haya conflicto.
git config --global pull.rebase true

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

## Crear y corregir (amend) commits

Tomar una fotografía del estado actual del proyecto (hacer un commit)

```zsh
#Toma una fotografía de los archivos en el escenario.
git commit -m "Comentario descriptivo en le commit"

#Añade todos los archivos al stage y les tota una fotografía (equivale a "add ." sequido del un "commit -m", sólo añade los archivos a los que se les ha dado seguimiento, pero que tienen cambios pendientes).
git commit -am "Comentario descriptivo en le commit"

#Cambia (corrige) el comentario del último commit por "Nuevo comentario descriptivo".
git commit --amend -m "Nuevo comentario descriptivo"

#Abre el editor por defecto (vim, nvim, etc.) para editar manualmente la info. (comentario, cambios en el commit, etc.) del último commit.
git commit --amend
```

El parámetro `--amend` se puede usar también para añadir archivos adicionales al `commit` original. Para esto, se añaden los archivos al `stage` y se ejecutan uno de los dos comandos anteriores para concretar la corrección.

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

#Igual que el anterior, pero sólo deshace los cambios en el archivo "nomb-archivo".
git git checkout -- nomb-archivo

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

#Además de motrar las ramas en el repo local, también muestra las ramas en el repo remoto.
git branch -a

#Muestra la rama actual en el repo local y la rama a la cual apunta en el repo remoto. Además, muestra información adicional del estado del proyecto.
git status

#También muestra esta información.
git log
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

- Ambas ramas "nombre-rama1" y "nombre-rama2" tienen commits que no están presentes en la otra, pero las modificaciones están presentes en las mismas lines de los mismos archivos (si además hay cambios como en el caso anterior, estos se resuelven de manera automática). En este caso, **Git** no es capás de mezclar toda la información de manera automtica (hay conflicto). Por tanto, hay que editar manualmente los archivos donde hay conflicto para solucionarlo. Las lineas donde hay conflicto apareceran duplicadas y remarcadas (una por cada rama) para facilitar la edición. Es muy recomendable usar editores como **VSCode** porque resaltan las diferencias con colores, además provee algunos botones con opciones predeterminadas para la resolución del conflicto. Finalmente, hay que hacer un commit con el resultado de la solución del conflicto.

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

## Almacenamiento del trabajo en progreso (Stash)

```zsh
#Almacena todos los cambios posteriores al último commit y reestablece el estado del proyecto (último commit).
git stash

#Recupera los cambios guardados en el último "stash" y elimina a ese "stash" si no hay conflicto. En caso de conflicto, el stash se tendrá que eliminar manualmente después de resolverlo.
git stash pop

#Muestra la lista de todos los stash creados. Los elementos de las lista están identificados por "stash@{N}", N ={0, 1,...}. Donde 0 corresponde al último stash.
git stash list

#Mostra información adicional del "stash@{N}".
git stash show stash@{N}

#Es equivalente a "git stash show stash@{0}".
git stash show

#Muestr información adicional de todos los elementos de la lista.
git stash list --stat

#Restaura el estado del proyecto almacenado en "stash@{N}". No elimina a "stash@{N}". La eliminación tendrá que ser manual.
git stash apply stash@{N}

#Elimina a "stash@{N}".
git stash drop stash@{N}

#Equivale a "git stash drop stash@{0}".
git stash drop

#Elimina a todos los stash creados.
git stash clear
```

Al recuperar los `stash`, pueden surgir comflictos. Estos se gestionan de manera similar a los conflictos con `merge`.

No es recomendable abusar de los `stash`, puesto que son muy confusos y complejos de gestionar. El `stash` debe tratarse como un almacen temporal, que permite almacenar modificaciones incompletas del proyecto (que no están listas para su uso) y que no se desean registrar mediante un commit en la historia del repo. Hay situaciones en la que esto puede ser útil (por ejem: cambiar de rama cuando hay modificaciones no registradas en un commit). Una vez finalizada la siguación, se recomiendo recuperar el estado del `stash` y eliminarlo.

## Repositorio remotos (GitHub, GitLab, etc.)

Descargar (clonar) un repo remoto.

```zsh
#Clona el repo remoto "nomb-repo" mediante su url.
git clone https://nomb-dominio-plataforma/nomb-usuario/nomb-repo.git

#Clona el repo mediante un tunel ssh (requiere configuración previa) para establecer la conexión (no es necesario, aqunque posible, introducir usuario y contraseña).
git clone git@nomb-dominio-plataforma:luislmv/nomb-usuario/nomb-repo.git
```

Conectar el repo remoto y el local.

```zsh
#Crea un alias "nomb-origen" a la url del repo remoto "nomb-repo". Requiere introducir usuario y contraseña cada vez que interactuemos con el repo remoto. Se puede configurar VSCode para que inicie sesión automáticamente por nosotros.
git remote add nomb-origen https://nomb-dominio-plataforma/nomb-usuario/nomb-repo.git

#Igual que el anterior, pero usa un tunel ssh (requiere configuración previa) para establecer la conexión (no es necesario, aqunque posible, introducir usuario y contraseña).
git remote add nomb-origen git@nomb-dominio-plataforma:luislmv/nomb-usuario/nomb-repo.git

#Muestra todos los alias y las url de los repos remotos.
git remote -v

#Además de lo anterior, muestra todas las ramas remotas y que ramaslocales están configuradas para realizar push (pull) hacia (desde) alguna rama remota.
git remote show nomb-origen
```

Los nombres de los alias son arbitrarios. No obstant, al repo remoto habitual (al que subimos cambios) se le suele llamar `origin`. Mientras que al repo del cual sólo obtenermos información (no hacemos cambios) se le suele llamar `upstream`.

Un ejemplo típico es cuando hacemos un fork (`origin`) de un repo (`upstream`) y queremos actualizar nuestro `origin` con iformación nueva añadida en `upstream`. En ese caso necesitamos manejar ambas fuentes.

Se pueden añadir todos los "alias" a repos remotos com se desee (por ejem. `origin` y `upstream`).

```zsh
#Crea un alias "nomb-origen-2" a la url de otro repo remoto "nomb-repo-2".
git remote add nomb-origen-2 https://nomb-dominio-plataforma/nomb-usuario/nomb-repo-2.git
```

El comando `git remote` ademaś de creaer un alias para la url de un repo remoto, también establece la conexión con este, de modo que podemos comparar los estados de ambos repos, actualizarlos, etc. Por otra parte, es posible asociar varios repos (que pudieran estar en distintas plataformas o no) a un sólo "alias". Esto permite sincronizar varios repos remotos al mismo tiempo.

```zsh
#Esto añade la nueva url (en la plataforma "nomb-dominio-plataforma-2") al alias anterior "nomb-origen".
git remote set-url --add nomb-origen https://nomb-dominio-plataforma-2/nomb-usuario/nomb-repo.git
```

Actualizar el repo remoto desde el repo local.

```zsh
#Actualiza la rama "nomb-rama" del repo remoto "nomb-origen".
git push nomb-origen nomb-rama

#Establece la rama "nomb-rama" de "nomb-origen" como "--set-upstream" y raaliza un push sobre ella. Esto permite hacer futuros push sobre la rama del repo remoto "nomb-origen" sin especificarla. Se puede establecer -u a todas las ramas que se requieran.
git push -u nomb-origen nomb-rama

#Hace push a todas las ramas especificadas por el comando anterior.
git push

#Hace push a todas las ramas del repo (con o sin --set-upstream).
git push --all

#Hace push de manera forzada (--force). Esto es últil si hemos modificado la historia (rebase, editamos, agregamos o eliminamos commits) del repo local y queremos que esas modificaciones se reflejen en el repo remoto (que conserva la historia original del repo).
git push -f

#Elimina la rama "nomb-rama" del repo remoto "nomb-origen".
git push -d nomb-origen :nomb-rama

#Igual que el anterior.
git push nomb-origen :nomb-rama

#Cambia el nombre (elimina la rama y crea una con el nuevo nombre) de la rama "nomb-rama" por "nuevo-nomb-rama" en el repo remoto nomb-origen. Se recomienda cambiar primero el nombre de la rama en el repo local a "nuevo-nomb-rama" para que sea clara la correspondencia con el repo remoto.
git push nomb-origen :nomb-rama nuevo-nomb-rama

# Hace push a todos los tags en el repo local (Los tags no se suben de manera automática al repo remoto al hacer push sobre una rama. Por tanto, hay que ejecutar este comando explícitamente para enviar los tags al repo remoto.)
git push --tags
```

Actualizar el repo local desde el repo remoto.

```zsh
#Actualiza (limpia) el registro de las ramas del repo remoto que ya no existen en el repo local.
git remote prune origin

#Actualiza el registro de la historia (log) del repo local con la historia del repo remoto. Sólo se actualiza el registro, no la historia, es decir, no se agregan los nuevos commits.
git fetch

#Despues de un "fetch" actualiza la rama activa en el repo local con la rama "nomb-rama" en el repo remoto "nomb-origen".
git merge nomb-origen/nomb-rama

#Actualiza la rama "nomb-rama" (el registro de todo el repo y todos los commits de "nomb-rama") del repo local desde el repo remoto "nomb-origen". No es necesario realizar un "fetch" antes, pull lo hace todo. De hecho, "pull" equivale a un "fetch" seguido de un "merge".
git pull nomb-origen nomb-rama

#Actualiza la rama actual si esta se ha establecido como "--set-upstream" en un push previo.
git pull

#Crea una la rama "nuev-rama-local" en el repo local basada en la rama "rama-remota" del repo remoto "nomb-origen" y desplaza el HEAD a ella. Es necesario tener previamente actualizado el registro (fetch o pull) con la info de la rama remota.
git checkout -b nuev-rama-local nomb-origen/rama-remota
```
