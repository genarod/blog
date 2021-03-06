Title: Gestores de contraseñas
Language: es
Date: 2020-04-23
Slug: password-managers
Tags: KeePass, Passwords, Contraseñas, Herramientas
Category: Herramientas
Summary: Gestores de contraseñas

Los gestores de contraseñas son herramientas que nos permiten tener muchas contraseñas guardadas en una base de datos encriptada.
Para acceder a esa base de datos necesitaremos una contraseña maestra pero esa será (casi) la única contraseña que deberemos recordar
(para acceder al gestor de contraseñas probablemente debimos haber introducido antes la contraseña del ordenador).

<img src="https://genarod.github.io/blog/images/padlock-key-lock-security-455x250.jpg"
     alt="Buenas prácticas de seguridad informática" width="455" height="250" />

# Ejemplos de gestores de contraseñas

Los más usados son [1Password](https://1password.com) y [LastPass](https://www.lastpass.com) y ambos son excelentes. Creo que 1Password es el líder del mercado pero LastPass es muy utilizado también.
Ambos se encargarán de almacenar todas tus contraseñas. Tú solamente debes recordar la contraseña del servicio que uses y el resto de tus contraseñas serán recordadas por el servicio que uses.
Tienen aplicaciones para iOS y Android, para Windows, macOS y Linux y extensiones para navegadores Safari, Chrome y Firefox.
Estas extensiones y las aplicaciones son muy convenientes puesto que se encargarán de llenar los campos de usuarios y contraseñas en los formularios de login automáticamente.
Tienen la capacidad para generar contraseñas fuertes y diferentes para cada diferente servicio que uses por lo que no tienes que volver a reutilizar contraseñas.
Ambos servicios son de pago pero LastPass tiene una opción gratuita que probablemente incluya las características que necesiten mucho usuarios.

Otros gestores de contraseñas son los que desarrollados como software libre como [KeePass](https://keepass.info) (que es el que yo uso) y
[PasswordSafe](https://pwsafe.org/index.shtml) (diseñado y recomendado por el reconocido experto en seguridad informática [Bruce Schneier](https://www.schneier.com/academic/passsafe/)).
El uso de software libre hace que el código fuente de estas herramientas esté disponible a cualquiera y que pueda ser auditado.
Estos proyectos están disponibles solamente para Windows pero existen proyectos que se basan en los proyectos originales para producir versiones para Linux, macOS, iOS y Android.

Yo utilizo macOS en mi portátil y por eso uso [KeePassXC](https://keepassxc.org) como aplicación de escritorio. En mi teléfono utilizaba [MiniKeePass](https://apps.apple.com/app/id451661808)
pero está siendo descontinuada y ahora mismo estoy decidiendo entre [StrongBox](https://strongboxsafe.com) y [KeePassium](https://keepassium.com).

Con este tipo de gestores tengo que tomar más decisiones. La aplicación simplemente se encarga de gestionar la base de datos de contraseñas.
No hay extensiones para que el navegador llene formularios por lo que eso se logra copiando, pegando y cambiando de una aplicación a la otra.
Por otra parte, como la base de datos no se comparte automáticamente entre mi ordenador y mi teléfono, yo tengo que decidir cómo hago para llevar la base de datos de un ordenador a otro.

LastPass y 1Password son mucho más fáciles de usar, como puedo instalar aplicaciones en mi ordenador y mi teléfono es muy fácil usarlo en todo momento y
probablemente sean más apropiados para usuarios sin mucha experiencia informática o que no quieran dedicar unas horas a entender cómo cambiar los flujos de trabajo.

Cuando empecé a utilizar un gestor de contraseñas mis restricciones eran muy diferentes y, sin acceso a dólares,
preferí la opción que me garantizaba acceso a mis contraseñas sin importar que la compañía que me ofreciera ese gestor de contraseñas de modelo de negocio.
Ahora la evaluación tal vez sería muy diferente, pero ahora tengo mis flujos de trabajo establecidos y no pienso cambiarme.

# (Algunas de) tus contraseñas (probablemente) ya han sido robadas

La página web [have I been pwned](https://haveibeenpwned.com) nos permite saber si nuestras contraseñas se han filtrado.
Yo he utilizado esa página para saber que algunos de mis amigos tienen contraseñas robadas.
Adicionalmente tanto Firefox como Chrome y Safari ofrecen una auditoría de nuestras contraseñas para verificar si son seguras y proveen gestores de contraseñas integrados.
Yo prefiero una herramienta dedicada que me permita usar mi base de datos de contraseñas en mi escritorio y mi teléfono y que me permita seguir usándola si mi ordenador es Windows, macOS o Linux.

Pero lo crucial de saber que alguna de tus contraseñas ha sido robada es que si no he utilizado esa contraseña en otra página web simplemente debo cambiar esa contraseña.
Si he usado esa contraseña en otras páginas web debo cambiar la contraseña de todas esas otras páginas además de la página que tuvo la filtración.

Por todo esto es crucial no reutilizar contraseñas ni contraseñas parecidas entre distintas páginas web. En la sección de [ataques a contraseñas](#ataques-a-contraseñas) explico cómo se

# Contraseña maestra

Al usar un gestor de contraseñas debo usar una contraseña maestra para desencriptar mis contraseñas. Elegir esa contraseña maestra es crucial para el uso de un gestor de contraseñas.

Este [artículo](https://medium.com/@stuartschechter/before-you-use-a-password-manager-9f5949ccf168) recomienda varias prácticas para utilizar gestores de contraseñas.

La contraseña maestra no la debo utilizar para nada más. Durante este artículo lo voy a repetir la oración anterior una docena de veces. Reutilizar contraseñas es peligrosísimo.
Reutilizar la contraseña que permite abrir el resto de mis contraseñas es derrotar el propósito de un gestor de contraseñas.

La contraseña maestra debe ser larga y aleatoria con al menos 12 caracteres en minúsculas o 5 palabras.

Probablemente deba usar mi contraseña maestra entre 10 y 30 veces antes de poder destruir el papel donde tengo anotada la contraseña maestra.

Si utilizo 1Password o LastPass, esos gestores de contraseñas proveen mecanismos para recuperar la contraseña maestra.
Si utilizo PasswordSafe o KeePass no voy a tener ningún mecanismo para recuperar la contraseña maestra y eso es parte de su diseño por lo que no cambiará en la próxima versión.
Eso los hace más seguros pero menos convenientes. Debo tener esto en cuenta al elegir el gestor de contraseñas que voy a usar.

# Contraseñas generadas y su uso en otros servicios

Las contraseñas que generaré en mi gestor de contraseñas para ser usadas en otros servicios deben tener al menos 16 caracteres. Esos caracteres deben contener mayúsculas, minúsculas y dígitos numéricos.

Contraseñas de menor longitud son menos seguras. Contraseñas de 8 caracteres o menos son muy débiles y no deben usarse por ninguna razón.

Muchas páginas web ofrecen la opción de usar contraseñas o darse de alta con Google o Facebook. Si uso un gestor de contraseñas puedo usar el generador de contraseñas para estos servicios sin que sea un problema.
Si no uso un gestor de contraseñas puedo usar Google o Facebook para darme de alta porque en este caso estoy confiando en las prácticas de seguridad de esas empresas.

Para casos como instituciones financieras es común que se ofrezca la opción de utilizar una aplicación de tipo autenticador que generará unos números aleatorios cada cierto tiempo que debo instalar en mi teléfono.
Si existe esa opción es preferible usarla.

No es recomendable usar aplicaciones que utilicen mensajes de texto SMS a mi teléfono para autenticarme. Recientemente se han dado muchos casos de que estafadores han conseguido que
las operadoras telefónicas redirijan los mensajes de texto a sus teléfonos para burlar estas medidas.

#  <a id="ataques-a-contraseñas"></a>Cómo funcionan los ataques a contraseñas

En esta sección voy a explicar brevemente cómo puede un "hacker" obtener una de nuestras contraseñas. Es muy muy sencillo para alguien con un poco de habilidad con los ordenadores.
Esto lo explico para explicar por qué no debo reutilizar mis contraseñas ni debo utilizar contraseñas parecidas.
Si la misma contraseña, o una contraseña parecida, la voy a usar en la página web de un supermercado (por ejemplo) y en la página web de mi banco (por poner otro ejemplo)
basta con que un "hacker" logre obtener las contraseñas de ese supermercado para obtener miles de contraseñas con correos electrónicos
que pueden utilizar para intentar ingresar en bancos. Esto no pasa porque me quieran robar a mí específicamente, sino esto se hace con cientos de miles de correos electrónicos.

Hay prácticas de desarrollo de software que evitan que esto sea tan sencillo como se muestra acá o en los artículos a los que apunto. La más básica es utilizar una sal para generar los hashes de las contraseñas.
Pero, ¿estamos seguros de que los programadores que hicieron la página web de ese supermercado utilizaron una buena sal? En la [lista](#bases-de-datos) de más abajo hay mas de 400 casos que no lo hicieron.

Para esta explicación voy a enlazar con algunos artículos que explican estos pasos con más detalle. Esos artículos están en inglés. Para seguir mi explicación no necesitas saber inglés.

Para hacerlo en mi ordenador debo bajarme un programa de recuperación de contraseñas como [Hashcat](https://hashcat.net/hashcat/), un diccionario con palabras comúnmente utilizadas en contraseñas
y la lista de contraseñas encriptadas que deseo desencriptar. Para encontrar diccionarios (también llamados wordlists) y una lista de contraseñas encriptadas para atacar solamente hacen falta
unos minutos de búsqueda en Google.

Este [artículo](https://arstechnica.com/information-technology/2013/03/how-i-became-a-password-cracker/) del año 2013 muestra cómo se podían efectuar esos ataques en minutos con el ordenador de casa.
Este otro [artículo](https://www.guru99.com/how-to-crack-password-of-an-application.html) es de este año incluye capturas de pantallas y muestra otras herramientas.

Este [artículo](https://hackernoon.com/20-hours-18-and-11-million-passwords-cracked-c4513f61fdb1) es del año pasado (2019) y muestra cómo hacer estos ataques con un ordenador alquilado en AWS (Amazon Web Services).
En 2 horas la mitad de las contraseñas fueron obtenidas, en 20 horas el 80% de las contraseñas fueron obtenidas, el precio de alquilar el ordenador usado fue de US$18,80.
El ordenador usado contaba con un GPU Nvidia Tesla K80 — a con 4992 núcleos que se podía alquilar en AWS por $0.90 por hora (P2.xlarge).
Ahora seguramente será posible usar más poder de cómputo por el mismo o menor precio.

Los ataques usados son de 4 niveles de dificultad:

- Palabras extraídas de un diccionario. Este no es el diccionario de la RAE sino un diccionario que incluye diccionarios comunes y contraseñas previamente encontradas
- Palabras seguidas o precedidas de números, letras o símbolos
- Palabras con sustitución de algunas letras por números como cambiar la letra "o" por el número "0"
- Múltiples palabras concatenadas
- Intentar todas las combinaciones de letras mayúsculas, minúsculas y números para contraseñas de pocos caracteres.

Este [artículo](https://towardsdatascience.com/password-cracking-is-easy-heres-how-to-do-it-875806a1e42a) muestra como se pueden intentar todas las combinaciones de 8 caracteres en pocas horas.
Si la contraseña tiene 16 caracteres tardaríamos trillones de años.

## <a id="bases-de-datos"></a>Bases de datos de contraseñas
Las bases de datos de contraseñas son listas de contraseñas encriptadas que se han publicado a partir de filtraciones. Acá hay [una lista](https://haveibeenpwned.com/PwnedWebsites) con algunas de esas filtraciones.
La lista incluye filtraciones de Avast, Badoo, Coachella, Disqus, Domino's de Bélgica y Francia, Dropbox, Forbes, imgur, LinkedIn, MySpace, Sephora, Snapchat, Tesco, tumblr, Yandex y
muchas páginas web de videojuegos, Bitcoin y pornografía entre más de 400 filtraciones. Algunas de estas filtraciones datan del año 2008 pero varias ocurrieron en el año 2020
(el presente artículo está redactado en Abril de 2020).

# Conclusión

Aunque aún debo manejar unas pocas contraseñas, la del ordenador y la de KeePass entre otras, el número de contraseñas que debo manejar es menor y por eso pueden ser más largas y aleatorias.
Por otra parte la contraseña que usaré en una página web en el que le compraré un juguete a mi hija no debe ser parecida a la que usaré en la página de mi banco.
Ambas contraseñas fueron generadas por mi gestor de contraseñas para ser una combinación aleatoria de letras y números de 16 o más caracteres.

Es importante seguir buenas prácticas de seguridad en Internet. Espero haber contribuido a que revises y mejores esas prácticas.
