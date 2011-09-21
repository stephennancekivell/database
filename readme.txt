I want to make a database for fun.

trying to make it fast should be fun.

This db needs to be persistant, to disk.
Could be some fun, file seeking here.

simple stdin-out interface, can be stateless, networked easily with nc. multiple connections, could be hard. cant use stdio for everything. async networking.

probably just throw stuff in a dict. Then update to disk.

dict of tables- table values where. each row can easily be tuple, stored by id in dict.

==Statements==

insert TABLE VARS
VARS is (column value, ..)

create table.
create_table TABLE_NAME (var type, ..)
select TABLE where EXPRESSION

EXPRESSION can be
COLUMN OPPERATOR VALUE
OPPERATER can be = !=
EXPRESSION && EXPRESSION
EXPRESSION || EXPRESSION

TABLE string alpha numeric chars. up to len 200. no space

== DATA TYPES ==
INT 
STRING up to 200 chars, enclosed in "", not escaped at all

==File Format==
Kinda want to be able to replace sections without re writing the whole thing. Thus needs to be binary ish.

This is where fixed size database scheames are nice.

Crashing at any point needs to keep everything safe.

To make this crash safe i can use a tmp file, storing what update im about to make to the DB file. On load the DB can check for the tmp file.

For the moment i wont consider the case where the database cannot fit in memory.

== road map ==
* syntax command parse
* store volatile
* store persistant
