#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class that contains the entry point of the command interpreter
    """

    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id"""
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in self.classes:
            print('** class doesn\'t exist **')
        else:
            new_instance = self.classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Print the string representation of an instance
        based on the class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in self.classes:
            print('** class doesn\'t exist **')
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key = f'{args[0]}.{args[1]}'
            all_objs = storage.all()
            if key not in all_objs:
                print('** no instance found **')
            else:
                print(all_objs[key])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in self.classes:
            print('** class doesn\'t exist **')
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key = f'{args[0]}.{args[1]}'
            all_objs = storage.all()
            if key not in all_objs:
                print('** no instance found **')
            else:
                del all_objs[key]
                storage.save()

    def do_all(self, arg):
        """
        Print all string representation of all instances
        based or not on the class name
        """
        args = arg.split()
        all_objs = storage.all()
        if len(args) == 0:
            for obj in all_objs.values():
                print(obj)
        elif args[0] not in self.classes:
            print('** class doesn\'t exist **')
        else:
            for obj in all_objs.values():
                if obj.__class__.__name__ == args[0]:
                    print(obj)

    def do_update(self, arg):
        """Update an instance based on the class name and id
        by adding or updating attribute"""
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in self.classes:
            print('** class doesn\'t exist **')
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key = f'{args[0]}.{args[1]}'
            all_objs = storage.all()
            if key not in all_objs:
                print('** no instance found **')
            elif len(args) == 2:
                print('** attribute name missing **')
            elif len(args) == 3:
                print('** value missing **')
            else:
                obj = all_objs[key]
                attr_name = args[2]
                attr_type = type(getattr(obj, attr_name, ''))
                attr_value = attr_type(args[3].strip('"'))
                setattr(obj, attr_name, attr_value)
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
