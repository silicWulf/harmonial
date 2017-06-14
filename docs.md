Harmonial - Discord Bot Creator
===================
Harmonial is a Python 3.5+ module that allows for the simple creation of Python Discord bots. Harmonial focuses to be easy to use with a vast array of functions at the users' disposal.

----------
Documentation
---------
------------
###Classes###

> harmonial.**Function**(*function_type*, *params=None*)

A `Function` class, which defines a bot function.

Parameters:

 - `function_type` (*str*) - The type of function that this class should be. A list of `function_type`s can be found at the bottom of the documentation.
 - `params` - The parameters that the function should have. *Different `function_type`s will require different variable types.*

>harmonial.**Command**(*commandname*, *functions*)

A `Command` class, which defines a bot command.

Parameters:

 - `commandname` (*str*) - The name of the command. This will be used to activate the `functions` by means of chat.
 - `functions` (list[`harmonial.Function`]) - A list of `Function`s that will be activated, in order, upon the command's activation.

--------------
###Functions###

>harmonial.**special**(*special_type*, *params=None*)

A function that returns data based on the `special_type` and `params` provided.

Parameters:

 - `special_type` (*str*) - A string that defines which function should be executed.
 - `params` - Parameters for the function.

>harmonial.**build**(*filename*, *prefix*, *commands*)

A function that compiles the list of `Command`s, `commands`, into finalized code. *Note: after compilation, you will need to supply a bot token in the generated file.*

Parameters:
 - `filename` (*str*) - File path that the final bot code will be written to.
 - `prefix` (*str*) - Prefix for the commands.
 - `commands` (list[`harmonial.Command`]) - A list of commands that will be in the bot.

----------

###Function Types###

`function_type`:

 - `'say'`  - (*`params` as str*) Say a string `params` in the channel as a response.
 - `'writeFile'` - (*`params` as tuple*) Write a string `params[1]` to file path `params[0]`.
 - `'uploadFile'` - (*`params` as str or file object*) Upload a file `params` to the channel as a response.
 - `'define'` - (*`params` as tuple(str, \*)*) - Define a variable name `params[0]` with data `params[1]`.

`special_type`:

 - `'randomNumber'` - (*`params` as tuple*(*int, int* *)*) - Returns string combiner that will return a random number between the range as defined in the tuple.
 - `'contentsOf'` - (*`params` as str*) Returns the contents of a file at path `params`.
 - `'variableString'` - (*`params` as str*) Returns a string combiner that will return the result of a variable `params` in string form.
 - `'rawVariable'` - (*`params` as str*) Returns the raw contents of a variable `params`.