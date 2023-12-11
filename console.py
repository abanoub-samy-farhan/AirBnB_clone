#!/usr/bin/python3
"""Console of the Project"""
import sys
import cmd
import re
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    return shlex.split(arg)


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) " if sys.__stdin__.isatty() else ''
    file = None
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """Method used to customize the help message of the Quit command"""
        print("Quit command to exit the program\n")

    def do_EOF(self, args):
        """EOF command to exit the program"""
        return True

    def help_EOF(self):
        """Method used to customize the message of the EOF help"""
        print("EOF command to exit the program")

    def emptyline(self):
        """Condititonal method used while their are no args"""
        pass

    def do_create(self, args):
        """Creating an instance of a model"""
        argl = parse(args)
        if not argl:
            print("** class name missing **")
        elif argl[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            obj = eval(argl[0])()
            print(obj.id)
            storage.save()

    def do_show(self, args):
        """Show a specific instacne is found or not
        Usage: show <class> <id> or <class>.show(<id>)"""
        arglist = parse(args)
        all_objs = storage.all()
        if not arglist:
            print("** class name missing **")
        elif arglist[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arglist) == 1:
            print("** instance id missing **")
        elif f"{arglist[0]}.{arglist[1]}" not in all_objs:
            print("** no instance found **")
        else:
            print(all_objs[f"{arglist[0]}.{arglist[1]}"])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        argl = parse(args)
        all_objs = storage.all()
        if not argl:
            print("** class name missing **")
        elif argl[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif f"{argl[0]}.{argl[1]}" not in all_objs:
            print("** no instance found **")
        else:
            del all_objs[f"{argl[0]}.{argl[1]}"]
            storage.save()

    def do_all(self, args):
        """Prints all string representation of all
        instances based or not on the class name"""
        arglist = parse(args)
        obj_all = storage.all()
        if not arglist:
            print([str(obj) for obj in obj_all.values()])
        elif len(arglist) == 1 and (arglist[0] not in self.__classes):
            print("** class doesn't exist **")
        else:
            obj_list = [str(obj) for obj in obj_all.values()
                        if arglist[0] == obj.__class__.__name__]
            print(obj_list)

    def do_update(self, args):
        """Updates an instance based on the class name
           Usage: update <class name> <id>
           <attribute name> '<attribute value>'"""
        arglist = parse(args)
        obj_all = storage.all()
        if not arglist:
            print("** class name missing **")
        elif arglist[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arglist) == 1:
            print("** instance id missing **")
        elif f"{arglist[0]}.{arglist[1]}" not in obj_all:
            print("** no instance found **")
        elif len(arglist) == 2:
            print("** attribute name missing **")
        elif len(arglist) == 3:
            print("** value missing **")
        else:
            obj = obj_all[f"{arglist[0]}.{arglist[1]}"]
            value_type = type(obj.__class__.__dict__[arglist[2]])
            obj.__dict__[arglist[2]] = value_type(arglist[3])
            storage.save()

    def do_count(self, args):
        count = 0
        obj_all = storage.all()
        if args not in self.__classes:
            print("** class doesn't exist **")
        else:
            for obj in obj_all.values():
                if obj.__class__.__name__ == args:
                    count += 1
        print(count)

    def default(self, arg: str):
        """Defualt function"""
        functions = {
            "all": self.do_all,
            "count": self.do_count,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "show": self.do_show
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in functions:
                    formated_line = "{} {}".format(argl[0], command[1])
                    return functions[command[0]](formated_line)
        print("*** Unknown syntax: {}".format(arg))
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
