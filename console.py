#!/usr/bin/python3
"""Explain the HBnB console.py."""
from shlex import split
import cmd
from models import storage
import re
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_brace = re.search(r"\{(.*?)\}", arg)
    bracket = re.search(r"\[(.*?)\]", arg)
    if curly_brace is None:
        if bracket is None:
            return [i.strip(",") for i in split(arg)]
        else:
            exerl = split(arg[:brackets.span()[0]])
            etl = [i.strip(",") for i in exerl]
            etlr.append(brackets.group())
            return etlr
    else:
        exerl = split(arg[:curly_braces.span()[0]])
        etlr = [i.strip(",") for i in exerl]
        etlr.append(curly_braces.group())
        return etlr


class HBNBCommand(cmd.Cmd):
    """Explain command interpreter of HBNBCommand class.

    Attributes:
        prompt (str): displays as command prompt.
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
        """Execute nothing upon receiving an empty line and hit enter."""
        pass

    def default(self, arg):
        """Display as Default value when the input is invalid"""
        argdiction = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        same = re.search(r"\.", arg)
        if same is not None:
            argl = [arg[:same.span()[0]], arg[same.span()[1]:]]
            same = re.search(r"\((.*?)\)", argl[1])
            if same is not None:
                command = [argl[1][:same.span()[0]], same.group()[1:-1]]
                if command[0] in argdiction.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdiction[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit as command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF as signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Creates a new instance of BaseModel, saves it to JSON and prints the id.
        """
        argument = parse(arg)
        if len(argument) == 0:
            print("** class name missing **")
        elif argument[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argument[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Prints the string representation of an instance based on the class name and id.
        """
        argument = parse(arg)
        objdic = storage.all()
        if len(argument) == 0:
            print("** class name missing **")
        elif argument[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argument) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argument[0], argument[1]) not in objdic:
            print("** no instance found **")
        else:
            print(objdic["{}.{}".format(argument[0], argument[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Deletes an instance based on the class name and id."""
        argument = parse(arg)
        objdic = storage.all()
        if len(argument) == 0:
            print("** class name missing **")
        elif argument[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argument) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argument[0], argument[1]) not in objdic.keys():
            print("** no instance found **")
        else:
            del objdic["{}.{}".format(argument[0], argument[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Prints all string representation of all instances based or not on the class name."""
        argument = parse(arg)
        if len(argument) > 0 and argument[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            Eobjl = []
            for obj in storage.all().values():
                if len(argument) > 0 and argument[0] == obj.__class__.__name__:
                    Eobjl.append(obj.__str__())
                elif len(argument) == 0:
                    Eobjl.append(obj.__str__())
            print(Eobjl)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argument = parse(arg)
        coun = 0
        for obj in storage.all().values():
            if argument[0] == obj.__class__.__name__:
                coun += 1
        print(coun)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Updates an instance based on the class name and id by adding or updating attribute
        (save the change into the JSON file)."""
        argument = parse(arg)
        objdic = storage.all()

        if len(argument) == 0:
            print("** class name missing **")
            return False
        if argument[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argument) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argument[0], argument[1]) not in objdic.keys():
            print("** no instance found **")
            return False
        if len(argument) == 2:
            print("** attribute name missing **")
            return False
        if len(argument) == 3:
            try:
                type(eval(argument[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argument) == 4:
            obj = objdict["{}.{}".format(argument[0], argument[1])]
            if argument[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argument[2]])
                obj.__dict__[argument[2]] = valtype(argument[3])
            else:
                obj.__dict__[argument[2]] = argument[3]
        elif type(eval(argument[2])) == dict:
            obj = objdict["{}.{}".format(argument[0], argument[1])]
            for ke, va in eval(argument[2]).items():
                if (ke in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[ke]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[ke])
                    obj.__dict__[ke] = valtype(va)
                else:
                    obj.__dict__[k] = va
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
