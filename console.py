#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        lexer = split(arg[:brackets.span()[0]])
    else:
        lexer = split(arg[:curly_braces.span()[0]])

    retl = [i.strip(",") for i in lexer]
    retl.append(curly_braces.group() if curly_braces else brackets.group())
    return retl


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }

        match = re.search(r"\.", arg)
        if match:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict:
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)

        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

 class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def _validate_args(self, arg, expected_length, error_messages):
        """Validate command arguments."""
        arg_list = parse(arg)
        if len(arg_list) != expected_length:
            for message in error_messages:
                print(message)
            return None
        return arg_list

    def _get_object(self, class_name, object_id):
        """Get the object from the storage."""
        obj_key = f"{class_name}.{object_id}"
        obj_dict = storage.all()
        return obj_dict.get(obj_key)

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        arg_list = self._validate_args(arg, 1, ["** class name missing **", "** class doesn't exist **"])
        if arg_list:
            instance = eval(arg_list[0])()
            print(instance.id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        arg_list = self._validate_args(arg, 2, ["** class name missing **", "** class doesn't exist **", "** instance id missing **"])
        if arg_list:
            obj = self._get_object(arg_list[0], arg_list[1])
            if obj:
                print(obj)
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        arg_list = self._validate_args(arg, 2, ["** class name missing **", "** class doesn't exist **", "** instance id missing **"])
        if arg_list:
            obj_dict = storage.all()
            obj_key = f"{arg_list[0]}.{arg_list[1]}"
            if obj_key in obj_dict:
                del obj_dict[obj_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        arg_list = self._validate_args(arg, 0, ["** class doesn't exist **"])
        if arg_list:
            obj_list = [str(obj) for obj in storage.all().values() if not arg_list or arg_list[0] == obj.__class__.__name__]
            print(obj_list)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        arg_list = self._validate_args(arg, 1, ["** class doesn't exist **"])
        if arg_list:
            count = sum(1 for obj in storage.all().values() if arg_list[0] == obj.__class__.__name__)
            print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        arg_list = self._validate_args(arg, 3, ["** class name missing **", "** class doesn't exist **", "** instance id missing **", "** attribute name missing **"])
        if arg_list:
            obj = self._get_object(arg_list[0], arg_list[1])
            if obj:
                if len(arg_list) == 3:
                    setattr(obj, arg_list[2], eval(arg_list[2]))
                else:
                    for key, value in eval(arg_list[2]).items():
                        setattr(obj, key, value)
                storage.save()
            else:
                print("** no instance found **")

        if len(argl) == 4:
            obj = objdict[f"{argl[0]}.{argl[1]}"]
            if argl[2] in obj.__class__.__dict__:
                val_type = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = val_type(argl[3])
            else:
                obj.__dict
