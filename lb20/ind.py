#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import os.path
import sys


def add_students(staff, name, group, estimation):
    """
    Добавить данные о студенте.
    """
    staff.append(
        {
            "name": name,
            "group": group,
            "estimation": estimation
        }
    )
    return staff


def display_students(staff):
    """
    Отобразить список студентов.
    """
    # Проверить, что список студентов не пуст.
    if staff:
        # Заголовок таблицы.
        line = "+-{}-+-{}-+-{}-+-{}-+".format("-" * 4, "-" * 30, "-" * 20, "-" * 8)
        print(line)
        print(
            "| {:^4} | {:^30} | {:^20} | {:^8} |".format(
                "№", "Ф.И.О.", "Группа", "Оценка"
            )
        )
        print(line)

        # Вывести данные о всех студентов.
        for idx, student in enumerate(staff, 1):
            print(
                "| {:>4} | {:<30} | {:<20} | {:>8} |".format(
                    idx,
                    student.get("name", ""),
                    student.get("group", 0),
                    student.get("estimation", 0),
                )
            )
            print(line)
    else:
        print("Список студентов пуст.")


def select_students(staff, period):
    """
    Выбрать студентов с нужным фамилией.
    """
    result = []
    for i in staff:
        if period in i.get("name").lower():
            result.append(i)
    return result


def save_workers(file_name, staff):
    """
    Сохранить всех студентов в файл JSON.
    """
    with open(file_name, "w", encoding="utf-8") as fout:
        json.dump(staff, fout, ensure_ascii=False, indent=4)


def load_students(file_name):
    """
    Загрузить всех студентов из файла JSON.
    """
    with open(file_name, "r", encoding="utf-8") as fin:
        return json.load(fin)


def main(command_line=None):
    file_parser = argparse.ArgumentParser(add_help=False)
    file_parser.add_argument("filename", action="store", help="The data file name")
    parser = argparse.ArgumentParser("students")
    parser.add_argument("--version", action="version", version="%(prog)s 0.1.0")
    subparsers = parser.add_subparsers(dest="command")
    add = subparsers.add_parser("add", parents=[file_parser], help="Add a new student")
    add.add_argument(
        "-n", "--name", action="store", required=True, help="The student's name"
    )
    add.add_argument(
        "-g",
        "--group",
        action="store",
        type=int,
        required=True,
        help="The student's group"
    )
    add.add_argument(
        "-e",
        "--estimation",
        action="store",
        type=int,
        required=True,
        help="The student's estimation"
    )
    _ = subparsers.add_parser(
        "display",
        parents=[file_parser],
        help="Display all students"
    )
    select = subparsers.add_parser(
        "select",
        parents=[file_parser],
        help="Select the students"
    )
    select.add_argument(
        "-P",
        "--period",
        action="store",
        type=int,
        help="The required period"
    )
    args = parser.parse_args(command_line)
    is_dirty = False
    if os.path.exists(args.filename):
        students = load_students(args.filename)
    else:
        students = []
    if args.command == "add":
        students = add_students(students, args.name, args.group, args.est)
        is_dirty = True
    elif args.command == "display":
        display_students(students)
    elif args.command == "select":
        selected = select_students(students, args.period)
        display_students(selected)
    if is_dirty:
        save_workers(args.filename, students)

    if __name__ == "__main__":
        main()
