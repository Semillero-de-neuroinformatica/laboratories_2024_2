
# Comandos más utilizados de Git
## Configuración del Usuario
* `git config --global user.name "[firstname lastname]"`\: Configura el nombre del usuario que se asociará con los commits\.
```warp-runnable-command
git config --global user.name <name>
```
* `git config --global user.email "[valid-email]"`\: Configura el correo electrónico del usuario\.
```warp-runnable-command
git config --global user.email <valid-email>
```
* `git config --global user.password "[personal-access-token]"`\: Configura el token de acceso del usuario
```warp-runnable-command
git config --global user.password <personal-access-token>
```
* `git config --gloabl --list`\: Permite listar toda la configuración global del repositorio git
```warp-runnable-command
git config --global --list
```
* `git config --list`\: Permite listar toda la configuraciónn local del repositorio de git
```warp-runnable-command
git config --global
```
## Configuración e Inicialización
* `git init`\: Inicializa un nuevo repositorio de Git en el directorio actual\.
```warp-runnable-command
git init
```
* `git clone [url]`\: Clona un repositorio completo desde una ubicación remota usando una URL\.
```warp-runnable-command
git clone <url>
```
## Etapas y Instantáneas \(Stage \& Snapshot\)
* `git status`\: Muestra el estado de los archivos en el directorio de trabajo y qué archivos están listos para ser commitados\.
```warp-runnable-command
git status
```
* `git add [file]`\: Agrega un archivo específico a la etapa \(stage\) para ser incluido en el próximo commit\. Si queremos añadir todos los archivos simplemente ponemos un punto \(\.\)
```warp-runnable-command
git add .
```
* `git reset [file]`\: Elimina un archivo de la etapa\, pero mantiene sus cambios en el directorio de trabajo\.
```warp-runnable-command
git reset <file>
```
* `git diff`\: Muestra las diferencias entre lo que está en el directorio de trabajo y lo que está en la etapa\.
```warp-runnable-command
git diff
```
* `git diff --staged`\: Muestra las diferencias entre lo que está en la etapa y lo que se ha commitado\.
```warp-runnable-command
git diff --staged
```
* `git commit -m "[descriptive message]"`\: Realiza un commit de los archivos en la etapa con un mensaje descriptivo\.
```warp-runnable-command
git commit -m <message>
```
## Ramas y Fusión \(Branch \& Merge\)
* `git branch`\: Lista todas las ramas en el repositorio\, y marca la rama activa con un asterisco\.
```warp-runnable-command
git branch
```
* `git branch [branch-name]`\: Crea una nueva rama a partir del commit actual\.
```warp-runnable-command
git branch <branch-name>
```
* `git checkout`\: Cambia a otra rama y actualiza el directorio de trabajo\.
```warp-runnable-command
git checkout <branch-name>
```
* `git merge [branch]`\: Fusiona la rama especificada con la rama actual\.
```warp-runnable-command
git merge <branch-name>

```
## Inspeccionar y Comparar \(Inspect \& Compare\)
* `git log`\: Muestra el historial de commits para la rama actualmente activa\.
```warp-runnable-command
git log
```
* `git log branchB..branchA`\: Muestra los commits en `branchA` que no están en `branchB`\.
```warp-runnable-command
git log <branch-name-B>..<branch-name-A>
```
* `git log --follow [file]`\: Muestra los commits que cambiaron un archivo\, incluso a través de renombramientos\.
```warp-runnable-command
git log --follow <file-name>
```
* `git diff branchB..branchA`\: Muestra las diferencias entre lo que está en `branchA` y lo que está en `branchB`\.
```warp-runnable-command
git diff <branch-name-B>..<branch-name-A>
```
* `git show`\: Muestra cualquier objeto de Git en formato legible por humanos\.
```warp-runnable-command
git show
```
## Compartir y Actualizar \(Share \& Update\)
* `git remote add [alias] [url]`\: Agrega una URL de Git como un alias\.
```warp-runnable-command
git remote add <alias> <url>
```
* `git fetch [alias]`\: Recupera todas las ramas del repositorio remoto\.
```warp-runnable-command
git fetch <alias>
```
* `git push [alias] [branch]`\: Envía los commits locales a la rama de un repositorio remoto\.
```warp-runnable-command
git push <alias> <branch>
```
* `git pull [alias] [branch]`\: Extrae y fusiona desde el repositorio remoto\.
```warp-runnable-command
git pull <alias> <branch>
```
## Seguimiento de Cambios de Rutas \(Tracking Path Changes\)
* `git rm [file]`\: Elimina el archivo del proyecto y lo coloca en la etapa para el commit\.
```warp-runnable-command
git rm <file-name>
```
* `git mv [existing-path] [new-path]`\: Cambia una ruta de archivo existente y lo coloca en la etapa\.
```warp-runnable-command
git mv <existing-path> <new-path>
```
* `git log --stat -M`\: Muestra todos los logs de commits con la indicación de cualquier ruta que se haya movido\.
```warp-runnable-command
git log --stat -M
```
## Ignorar Patrones \(Ignoring Patterns\)
* `logs/`\, `*.notes`\, `pattern/`\: Guarda un archivo con los patrones deseados como `.gitignore` para evitar que se envíen a la etapa archivos coincidentes\.
* `git config --global core.excludesfile [file]`\: Configura un archivo de patrón de ignorancia global para todos los repositorios locales\.
```warp-runnable-command
git config --global core.excludesfile <fila-name>

```
## Reescribir Historia \(Rewrite History\)
* `git rebase [branch]`\: Aplica cualquier commit de la rama actual antes de la rama especificada\.
```warp-runnable-command
git rebase <branch-name>
```
## Commits Temporales \(Temporary Commits\)
* `git stash`\: Guarda cambios modificados y en la etapa\.
```warp-runnable-command
git stash
```
* `git stash list`\: Lista las modificaciones almacenadas en el stash\.
```warp-runnable-command
git stash list
```
* `git stash pop`\: Escribe el trabajo desde la parte superior del stash y lo aplica al directorio de trabajo\.
```warp-runnable-command
git stash pop
```
* `git stash drop`\: Descarta los cambios desde la parte superior del stash\.
```warp-runnable-command
git stash drop
```
\' \> git\_commands\.md