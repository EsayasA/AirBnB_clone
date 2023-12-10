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
    c_b = re.search(r"\{(.*?)\}", arg)
    bra = re.search(r"\[(.*?)\]", arg)
    if c_b is None:
        if bra is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:bra.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(bra.group())
            return retl
    else:
        lexer = split(arg[:c_b.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(c_b.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): command prompt.
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
        same = re.search(r"\.", arg)
        if same is not None:
            argu = [arg[:same.span()[0]], arg[same.span()[1]:]]
            same = re.search(r"\((.*?)\)", argu[1])
            if same is not None:
                command = [argu[1][:same.span()[0]], same.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argu[0], command[1])
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

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        para = parse(arg)
        if len(para) == 0:
            print("** class name missing **")
        elif para[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(para[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        para = parse(arg)
        odic = storage.all()
        if len(para) == 0:
            print("** class name missing **")
        elif para[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(para) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(para[0], para[1]) not in odic:
            print("** no instance found **")
        else:
            print(odic["{}.{}".format(para[0], para[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        para = parse(arg)
        odic = storage.all()
        if len(para) == 0:
            print("** class name missing **")
        elif para[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(para) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(para[0], para[1]) not in odic.keys():
            print("** no instance found **")
        else:
            del odic["{}.{}".format(para[0], para[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        para = parse(arg)
        if len(para) > 0 and para[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            ob = []
            for o in storage.all().values():
                if len(para) > 0 and para[0] == o.__class__.__name__:
                    ob.append(o.__str__())
                elif len(para) == 0:
                    ob.append(o.__str__())
            print(ob)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        para = parse(arg)
        coun = 0
        for o in storage.all().values():
            if para[0] == o.__class__.__name__:
                coun += 1
        print(coun)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        para = parse(arg)
        odic = storage.all()

        if len(para) == 0:
            print("** class name missing **")
            return False
        if para[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(para) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(para[0], para[1]) not in odic.keys():
            print("** no instance found **")
            return False
        if len(para) == 2:
            print("** attribute name missing **")
            return False
        if len(para) == 3:
            try:
                type(eval(para[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(para) == 4:
            o = odic["{}.{}".format(para[0], para[1])]
            if para[2] in o.__class__.__dict__.keys():
                valtype = type(o.__class__.__dict__[para[2]])
                o.__dict__[para[2]] = valtype(para[3])
            else:
                o.__dict__[para[2]] = para[3]
        elif type(eval(para[2])) == dict:
            o = odic["{}.{}".format(para[0], para[1])]
            for ke, va in eval(para[2]).items():
                if (ke in o.__class__.__dict__.keys() and
                        type(o.__class__.__dict__[ke]) in {str, int, float}):
                    valtype = type(o.__class__.__dict__[ke])
                    o.__dict__[ke] = valtype(va)
                else:
                    o.__dict__[ke] = va
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
