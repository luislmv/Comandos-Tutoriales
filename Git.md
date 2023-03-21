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
git config --global user.name "Luis Muñiz Valledor" 

#Establece el correo electrónico de mi usuario git.
git config --global user.email "muniz.valledor.luis@ciencias.unam.mx"

git config --global core.editor "nvim"

git config --global alias.s "status -sb"

git config --global alias.lg "log --oneline --decorate --all --graph"

git config --global init.defaultBranch main

git config --global core.autocrlf input

git config --global --list 

git config --global -e
```
